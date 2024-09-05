import React from 'react';
import { createClient } from '@/utils/supabase/server'
const supabase = createClient();
export default async function CreateBook() {
  return <main>CreateBook (Secure) - only logged in user can access</main>;
}
