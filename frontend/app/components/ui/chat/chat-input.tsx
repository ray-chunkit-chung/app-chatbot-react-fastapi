"use client";

import { ChatInput} from "@llamaindex/chat-ui";
// import { DocumentInfo, ImagePreview } from "@llamaindex/chat-ui/widgets";
// import { LlamaCloudSelector } from "./custom/llama-cloud-selector";
// import { useClientConfig } from "./hooks/use-config";

export default function CustomChatInput() {
  return (
    <ChatInput
      className="shadow-xl rounded-xl"
    >
      <ChatInput.Form>
        <ChatInput.Field />
        <ChatInput.Submit />
      </ChatInput.Form>
    </ChatInput>
  );
}
