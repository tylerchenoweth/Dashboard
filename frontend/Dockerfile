# Use the official Node.js image
FROM node:20

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package.json package-lock.json ./
RUN npm install

# Copy the rest of the app
COPY . .

# Expose Next.js default port
EXPOSE 3000

# Start Next.js
CMD ["npm", "run", "dev"]
