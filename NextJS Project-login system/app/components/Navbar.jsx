'use client';

import React from 'react';
import Image from 'next/image';
import Link from 'next/link';
import { usePathname } from 'next/navigation';
import Logo from './logo.svg';

// components
// Uncomment when supabase auth ready
import Profile from './Profile';

export default function Navbar() {
  const pathname = usePathname();

  return (
    <nav className="navbar">
      <div className="navbar-container">
        {/* Logo */}
        <div className="navbar-logo">
          <Image src={Logo} alt="Smart Storytime" width={230} quality={100} />
        </div>

        {/* Links in the center */}
        <div className="navbar-links">
          <Link
            href="/create-book"
            className={pathname.startsWith('/create-book') ? 'active' : ''}
          >
            Create book
          </Link>
          <Link
            href="/library"
            className={pathname.startsWith('/library') ? 'active' : ''}
          >
            Library
          </Link>
          <Link href="/guide">Guide</Link>
        </div>

        {/* Profile/Account Section */}
        <div className="navbar-account">
          {/* Comment when supabase auth ready}
          <Link href="/login">
            <button className="btn-outline primary w-20">Login</button>
          </Link>
          {Uncomment when supabase auth ready */}
          {<Profile />}
        </div>
      </div>
    </nav>
  );
}
