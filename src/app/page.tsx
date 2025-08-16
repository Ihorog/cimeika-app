"use client";

import React, { useEffect, useState } from "react";

export default function HomePage() {
  const [weather, setWeather] = useState("Loading...");
  const [time, setTime] = useState(new Date().toLocaleTimeString());
  const [astrology, setAstrology] = useState("Loading...");

  useEffect(() => {
    // Fetch weather data
    fetch(
      `https://api.openweathermap.org/data/2.5/weather?q=Kyiv&appid=${process.env.NEXT_PUBLIC_OPENWEATHER_API_KEY}&units=metric`
    )
      .then((res) => res.json())
      .then((data) => {
        setWeather(`${data.weather[0].description}, ${data.main.temp}°C`);
      })
      .catch(() => setWeather("Unable to fetch weather"));

    // Update time every second
    const interval = setInterval(() => {
      setTime(new Date().toLocaleTimeString());
    }, 1000);

    // Fetch astrology data (dummy example)
    fetch(
      `https://api.freeastrologyapi.com/forecast?sign=aries&apikey=${process.env.NEXT_PUBLIC_ASTROLOGY_API_KEY}`
    )
      .then((res) => res.json())
      .then((data) => {
        setAstrology(data.forecast || "No forecast available");
      })
      .catch(() => setAstrology("Unable to fetch astrology"));

    return () => clearInterval(interval);
  }, []);

  return (
    <div>
      <section className="text-center mb-12">
        <h1 className="text-4xl font-semibold mb-4">Ласкаво просимо до Організуй</h1>
        <p className="text-lg max-w-xl mx-auto mb-6">
          Ваш шлях до організованого та ефективного життя починається тут.
        </p>
        <button
          onClick={() => alert("Починаємо подорож!")}
          className="bg-black text-white px-6 py-3 rounded hover:bg-gray-800 transition"
        >
          Почати
        </button>
      </section>

      <section className="grid grid-cols-2 md:grid-cols-3 gap-6 max-w-4xl mx-auto mb-12">
        <a
          href="/event"
          className="border border-black rounded p-6 hover:bg-black hover:text-white transition text-center"
        >
          Події
        </a>
        <a
          href="/gallery"
          className="border border-black rounded p-6 hover:bg-black hover:text-white transition text-center"
        >
          Галерея
        </a>
        <a
          href="/mood"
          className="border border-black rounded p-6 hover:bg-black hover:text-white transition text-center"
        >
          Настрій
        </a>
        <a
          href="/child"
          className="border border-black rounded p-6 hover:bg-black hover:text-white transition text-center"
        >
          Дитина
        </a>
        <a
          href="/calendar"
          className="border border-black rounded p-6 hover:bg-black hover:text-white transition text-center"
        >
          Календар
        </a>
        <a
          href="/ci"
          className="border border-black rounded p-6 hover:bg-black hover:text-white transition text-center"
        >
          Ci
        </a>
      </section>

      <section className="max-w-4xl mx-auto">
        <h2 className="text-2xl font-semibold mb-4">Дані в реальному часі</h2>
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 text-center">
          <div className="border border-black rounded p-4">
            <h3 className="font-semibold mb-2">Погода</h3>
            <p>{weather}</p>
          </div>
          <div className="border border-black rounded p-4">
            <h3 className="font-semibold mb-2">Час</h3>
            <p>{time}</p>
          </div>
          <div className="border border-black rounded p-4">
            <h3 className="font-semibold mb-2">Астрологічний прогноз</h3>
            <p>{astrology}</p>
          </div>
        </div>
      </section>
    </div>
  );
}
