import type { NextApiRequest, NextApiResponse } from 'next';

export default async function handler(
  req: NextApiRequest,
  res: NextApiResponse
) {
  const sign = (req.query.sign as string) || 'aries';
  const apiKey = process.env.NEXT_PUBLIC_FREEASTROLOGYAPI_API_KEY;

  if (!apiKey) {
    res.status(500).json({ error: 'Missing FreeAstrologyAPI key' });
    return;
  }

  try {
    const response = await fetch(
      `https://api.freeastrologyapi.com/forecast?sign=${encodeURIComponent(sign)}&apikey=${apiKey}`
    );
    const data = await response.json();
    res.status(200).json(data);
  } catch (error: any) {
    res.status(500).json({ error: 'Failed to fetch astrological data' });
  }
}
