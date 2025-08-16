import React from "react";
import Header from "../components/Header";
import Footer from "../components/Footer";

export const metadata = {
  title: "Cimeika",
  description: "Clone of Cimeika website",
};

export default function RootLayout({
  children,
}: {
  children: React.ReactNode;
}) {
  return (
    <html lang="uk">
      <head>
        <link
          href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap"
          rel="stylesheet"
        />
      </head>
      <body className="bg-white text-black font-sans min-h-screen flex flex-col">
        <Header />
        <main className="flex-grow container mx-auto px-4 py-8">{children}</main>
        <Footer />
      </body>
    </html>
  );
}
