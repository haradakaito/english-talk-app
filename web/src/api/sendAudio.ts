export const sendAudio = async (audioBlob: Blob): Promise<string> => {
const arrayBuffer = await audioBlob.arrayBuffer();
const base64Audio = btoa(
    new Uint8Array(arrayBuffer).reduce((data, byte) => data + String.fromCharCode(byte), "")
);

const endpoint = "https://ygnddok5kc.execute-api.ap-northeast-1.amazonaws.com/v1/chat";

const res = await fetch(endpoint, {
    method: "POST",
    headers: {
    "Content-Type": "application/json",
    },
    body: JSON.stringify({ audio_base64: base64Audio }),
});

if (!res.ok) throw new Error(`API error: ${res.status}`);
return await res.text();
};
