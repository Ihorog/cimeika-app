import type { NextApiRequest, NextApiResponse } from 'next';

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  const city = (req.query.city as string) || 'London';
  const apiKey = process.env.NEXT_PUBLIC_OPENWEATHERMAP_API_KEY;

  if (!apiKey) {
    res.status(500).json({ error: 'Missing OpenWeatherMap API key' });
    return;
  }

  try {
    const response = await fetch(
      `https://api.openweathermap.org/data/2.5/weather?q=${encodeURIComponent(city)}&appid=${apiKey}&units=metric`
    );
    const data = await response.json();
    res.status(200).json(data);
  } catch (error: any) {
    res.status(500).json({ error: 'Failed to fetch weather data' });
  }
}
