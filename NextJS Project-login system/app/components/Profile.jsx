'use client';
import React, { useState, useEffect } from 'react';
import { useRouter } from 'next/navigation';
import { createClient } from '@/utils/supabase/client'; // Use the @ alias if working
import Link from 'next/link';
export default function Profile() {
  const [user, setUser] = useState(null);
  const [isDropdownOpen, setIsDropdownOpen] = useState(false);
  const router = useRouter(); // For navigation after logout

  // Check user login state
  useEffect(() => {
    const supabase = createClient();
    const getUser = async () => {
      const {
        data: { user },
      } = await supabase.auth.getUser();
      setUser(user);
    };

    getUser();
  }, []);

  const handleLogout = async () => {
    const supabase = createClient();
    await supabase.auth.signOut();
    setUser(null);
    router.push('/'); // Redirect to home after logout
    router.refresh();
  };

  return (
    <div className="navbar-account">
      {user ? (
        <div className="relative">
          {/* Avatar */}
          <button
            onClick={() => setIsDropdownOpen(!isDropdownOpen)}
            className="bg-purple-700 text-white rounded-full w-10 h-10 flex items-center justify-center text-xl"
          >
            {user.email[0].toUpperCase()}
          </button>

          {/* Dropdown Menu */}
          {isDropdownOpen && (
            <div className="absolute right-0 mt-2 w-48 bg-white rounded-md shadow-lg py-1 z-50">
              {/*<button
                //onClick={handleLogout}
                onClick={logout}
                className="block w-full text-left px-4 py-2 text-gray-700 hover:bg-gray-100"
              >
                Logout
              </button>*/}
              <form action={handleLogout}>
                <button
                  //onClick={handleLogout}
                  className="block w-full text-left px-4 py-2 text-gray-700 hover:bg-gray-100"
                >
                  Logout
                </button>
              </form>
            </div>
          )}
        </div>
      ) : (
        <Link href="/login">
          <button className="btn-outline primary w-20">Login</button>
        </Link>
      )}
    </div>
  );
}
