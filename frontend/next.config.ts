import type { NextConfig } from "next";

const nextConfig: NextConfig = {
    output: 'export',  // Enable static HTML export
    distDir: 'out',    // Specify output directory
    images: {
      unoptimized: true // Required for static export
    }
};

export default nextConfig;


