"use client";

import React from "react";
import Link from "next/link";

export default function Header() {
  return (
    <header className="bg-black text-white">
      <nav className="container mx-auto px-4 py-4 flex space-x-6">
        <Link href="/" className="hover:underline">
          Home
        </Link>
        <Link href="/event" className="hover:underline">
          Event
        </Link>
        <Link href="/gallery" className="hover:underline">
          Gallery
        </Link>
        <Link href="/mood" className="hover:underline">
          Mood
        </Link>
        <Link href="/child" className="hover:underline">
          Child
        </Link>
        <Link href="/calendar" className="hover:underline">
          Calendar
        </Link>
        <Link href="/ci" className="hover:underline">
          Ci
        </Link>
      </nav>
    </header>
  );
}
