import React from 'react';
import Image from 'next/image';
import Logo from '../../components/logo.svg';
import SignUpForm from "../../components/SignUpForm.jsx"
export default function Signup() {
  return (
    <div className="m-5 p-3 max-w-sm mx-auto bg-white rounded-lg">
      <Image src={Logo} />
      <SignUpForm />
    </div>
  );
}
