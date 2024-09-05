import {signup} from './actions'
import Link from 'next/link'
export default function SignUpForm(){
    return (
        <form>
          <div className="mb-5 mt-5">
            <p className="text-center font-bold text-xl">Signup to your account</p>
          </div>
          <div className="mb-5">
            <label htmlFor="email" className="block mb-2 font-bold">Email Address</label>
            <input name="email" type="email" id="email" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5" placeholder="Email Address" required />
          </div>
          <div className="mb-5">
            <label htmlFor="password" className="block mb-2 font-bold">Password</label>
            <input name="password" type="password" id="password" className="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg block w-full p-2.5" placeholder="Password" required />
          </div>
          <button type="submit" formAction={signup} className="mb-5 text-white bg-purple-700 hover:bg-purple-800 font-medium rounded-lg text-sm w-full px-5 py-2.5 text-center">Submit</button>
          <div className="mb-5 text-center font-light">
            <p>Have an account? <Link href="/login" className="text-blue-500">Login</Link></p>
          </div>
      </form>
    )
}