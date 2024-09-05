import React from 'react';
import Image from 'next/image';
import Logo from '../../components/logo.svg';
import LoginForm from '../../components/LoginForm.jsx';

export default function Login() {
  return (
      
    <div className="m-5 p-3 max-w-sm mx-auto bg-white rounded-lg">
      <Image src={Logo} />
      <LoginForm />
    </div>
  )
}
