#!/usr/bin/env node
import { GoogleGenerativeAI } from "@google/generative-ai";
import { GoogleAIFileManager } from "@google/generative-ai/server";

const apiKey = "AIzaSyD_SyHYr-ZLhl4vfDQqSHmgIGOGp-HJdT8";

// Initialize GoogleGenerativeAI with your API_KEY.
const genAI = new GoogleGenerativeAI(apiKey);
// Initialize GoogleAIFileManager with your API_KEY.
const fileManager = new GoogleAIFileManager(apiKey);

const model = genAI.getGenerativeModel({
  // Choose a Gemini model.
  model: "gemini-1.5-flash",
});

// Upload the file and specify a display name.
const uploadResponse = await fileManager.uploadFile("story.txt", {
  mimeType: "text/plain", // Changed from "application/txt" to "text/plain"
  displayName: "Gemini 1.5 TXT",
});

// View the response.
console.log(
  `Uploaded file ${uploadResponse.file.displayName} as: ${uploadResponse.file.uri}`
);

// Generate content using text and the URI reference for the uploaded file.
const result = await model.generateContent([
  {
    fileData: {
      mimeType: uploadResponse.file.mimeType,
      fileUri: uploadResponse.file.uri,
    },
  },
  { text: "Can you summarize this document as a bulleted list?" },
]);

// Output the generated text to the console
console.log(result.response.text());