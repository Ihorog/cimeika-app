"use client";

import React from "react";

export default function Footer() {
  return (
    <footer className="bg-black text-white py-4 mt-8">
      <div className="container mx-auto px-4 text-center">
        <p>&copy; 2023 Cimeika. All rights reserved.</p>
        <ul className="flex justify-center space-x-4 mt-2">
          <li>
            <a
              href="https://www.facebook.com/cimeika"
              target="_blank"
              rel="noopener noreferrer"
              className="hover:underline"
            >
              Facebook
            </a>
          </li>
          <li>
            <a
              href="https://www.twitter.com/cimeika"
              target="_blank"
              rel="noopener noreferrer"
              className="hover:underline"
            >
              Twitter
            </a>
          </li>
          <li>
            <a
              href="https://www.instagram.com/cimeika"
              target="_blank"
              rel="noopener noreferrer"
              className="hover:underline"
            >
              Instagram
            </a>
          </li>
          <li>
            <a href="mailto:contact@cimeika.com" className="hover:underline">
              Contact Us
            </a>
          </li>
        </ul>
      </div>
    </footer>
  );
}
