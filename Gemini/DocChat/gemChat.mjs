import { GoogleGenerativeAI } from "@google/generative-ai";

const apiKey = "AIzaSyD_SyHYr-ZLhl4vfDQqSHmgIGOGp-HJdT8";

const genAI = new GoogleGenerativeAI(apiKey);
const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });
const chat = model.startChat({
  history: [
    {
      role: "user",
      parts: [{ text: "Hello" }],
    },
    {
      role: "model",
      parts: [{ text: "Great to meet you. What would you like to know?" }],
    },
  ],
});
let result = await chat.sendMessage("I have 2 dogs in my house.");
console.log(result.response.text());
result = await chat.sendMessage("How many paws are in my house?");
console.log(result.response.text());