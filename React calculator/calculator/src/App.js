import Button from "./components/Button"
import ButtonBox from "./components/ButtonBox"
import Screen from "./components/Screen"
import Wrapper from "./components/Wrapper"
import './App.css';
const keys = [
  ["sin","cos","tan","!","^"],
  ["7","8","9","sqrt","del"],
  ["4","5","6","X","/"],
  ["1","2","3","+","-"],
  ["0",".","rand","%","="],
];
const App = () => {
  return (
    <Wrapper>
      <Screen value="0"/>
      <ButtonBox>
      {
          keys.flat().map((val) => {
            return(
              <Button 
                key={val}
                className={val === "=" ? "equals" : ""}
                value={val}
                onClick={() => {alert(`${val} clicked`)}}
              />
            )
          })
      }
      </ButtonBox>
    </Wrapper>
  )
}

export default App;
