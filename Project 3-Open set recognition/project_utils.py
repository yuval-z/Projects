def eval_model(model, data_loader, device):
    """ Evaluation function for the OSR task. 
    Given your OSR predictions, comptues the accuracy on MNIST, OOD set and both. 
    Note - this function does NOT computes the MNIST baseline accruacy. 
    Returns:
     - acc_mnist
     - acc_ood
     - acc_total
    """
    
    # Ensure model is in evaluation mode
    model.eval()

    correct_mnist = 0
    total_mnist = 0
    correct_ood = 0
    total_ood = 0

    # No need to track gradients for evaluation, saves memory and computations
    with torch.no_grad():
        for data, labels in data_loader:
            data, labels = data.to(device), labels.to(device)
            outputs = model(data)

            ### Modify output if needed ###

            # y pred should be a vector of size (N_batch,) -> [5, 2, ..., 10]
            # and not one-hot. You can handle this either in your model or here. 
            
            # Assuming the model returns an (N_batch, 11) size output
            probas, y_pred = torch.max(outputs, 1)
            
	    # Assuming the model retuns the predicted label (N_batch, ) 
	    # y_pred = outputs
	    
            # Split MNIST and OOD predictions and labels
            # Assuming numerical labels, which is MNIST/CIFAR datasets default
            # Note: Not one-hot! 
            mask_mnist = labels < 10
            mask_ood = ~mask_mnist
            labels_mnist = labels[mask_mnist]
            labels_ood = labels[mask_ood]

            pred_mnist = y_pred[mask_mnist]
            pred_ood = y_pred[mask_ood]

            total_mnist += labels_mnist.size(0)
            total_ood += labels_ood.size(0)
            correct_mnist += (pred_mnist == labels_mnist).sum().item()
            correct_ood += (pred_ood == labels_ood).sum().item()

    acc_mnist = correct_mnist / total_mnist
    acc_ood = correct_ood / total_ood
    acc_total = (correct_mnist + correct_ood) / (total_mnist + total_ood)

    return acc_mnist, acc_ood, acc_total


# Usaged example
# Load the MNIST and OOD datasets
# Define the transformations
mnist_transform = transforms.Compose([ ... ])

cifar_transform = transforms.Compose([ ... ])

mnist = MNIST(root='./data', train=False, download=True, transform=mnist_transform)
ood = CIFAR10(root='./data', train=False, download=True, transform=cifar_transform)

# sample ~500-1000 samples from CIFAR
# ... # 
# Combine the datasets
combined_ds = CombinedDataset(mnist, ood)
# large batchsize for inference is recommended
batch_size = 1024
data_loader = DataLoader(combined_ds, batch_size=batch_size, shuffle=True)


device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model.to(device)

acc_mnist, acc_ood, acc_total = eval_model(model, data_loader, device)
print(f'MNIST Accuracy: {acc_mnist*100:.2f}%')
print(f'OOD Accuracy: {acc_ood*100:.2f}%')
print(f'Total Accuracy: {acc_total*100:.2f}%')

