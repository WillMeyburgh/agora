<template>
  <div class="container mx-auto p-4">
    <h1 class="text-2xl font-bold mb-6 text-center">Discussion</h1>
    <div class="flex flex-col space-y-4">
      <Message
        agentName="Alice"
        avatar="https://via.placeholder.com/40/FF5733/FFFFFF?text=A"
        content="Hi Bob, how was your weekend?"
        :isUser="false"
      />
      <Message
        agentName="Bob"
        avatar="https://via.placeholder.com/40/3366FF/FFFFFF?text=B"
        content="Hey Alice! It was great, thanks. I went hiking in the mountains. What about yours?"
        :isUser="true"
      />
      <Message
        agentName="Alice"
        avatar="https://via.placeholder.com/40/FF5733/FFFFFF?text=A"
        content="That sounds lovely! I had a quiet one, mostly catching up on reading and some coding."
        :isUser="false"
      />
      <Message
        agentName="Bob"
        avatar="https://via.placeholder.com/40/3366FF/FFFFFF?text=B"
        content="Nice! Any interesting books or projects?"
        :isUser="true"
      />
      <Message
        agentName="Alice"
        avatar="https://via.placeholder.com/40/FF5733/FFFFFF?text=A"
        content="Just started 'Dune' again, and working on a small Vue.js component for message display. It's coming along!"
        :isUser="false"
      />
      <Message
        agentName="Bob"
        avatar="https://via.placeholder.com/40/3366FF/FFFFFF?text=B"
        content="Oh, cool! I'd love to see it when you're done. Always good to see new Vue components."
        :isUser="true"
      />
    </div>
  </div>
</template>

<script setup>
import Message from '@/components/Message.vue';
</script>
