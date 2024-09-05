'use server'

import { revalidatePath } from 'next/cache'
import { redirect, replace } from 'next/navigation'

import { createClient } from '@/utils/supabase/server'

export async function login(formData) {
  const supabase = createClient()

  // type-casting here for convenience
  // in practice, you should validate your inputs
  const data = {
    email: formData.get('email'),
    password: formData.get('password'),
  }

  const { error, errorInfo } = await supabase.auth.signInWithPassword(data)

  if (error) {
    console.log("Error in actions.js login");
    console.log({ error, errorInfo })
    redirect('/error')
  }

  revalidatePath('/', 'layout')
  redirect('/')
}

export async function signup(formData) {
  const supabase = createClient()

  const data = {
    email: formData.get('email'),
    password: formData.get('password'),
  }

  const { error, errorInfo } = await supabase.auth.signUp(data)

  if (error) {
    console.log("Error in actions.js signup");
    console.log({ error, errorInfo })
    redirect('/error')
  }

  revalidatePath('/', 'layout')
  redirect('/email-verification')
}