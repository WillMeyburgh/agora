<template>
  <div :class="['flex items-start mb-4', agentContainerClasses]">
    <div :class="['relative flex flex-col p-3 max-w-md', messageBubbleClasses]">
      <div class="font-bold mb-1 text-gray-800">{{ agentName }}</div>
      <div class="text-gray-700 leading-snug">{{ content }}</div>
    </div>
  </div>
</template>

<script setup>
import { defineProps, computed } from 'vue';

const props = defineProps({
  agentName: {
    type: String,
    required: true
  },
  avatar: {
    type: String,
    default: ''
  },
  content: {
    type: String,
    required: true
  },
  isUser: {
    type: Boolean,
    default: false
  },
  backgroundColor: {
    type: String,
    default: 'bg-gray-200' // Default background color
  }
});

const agentContainerClasses = computed(() => {
  return props.isUser ? 'ml-auto flex-row-reverse' : 'mr-auto';
});

const messageBubbleClasses = computed(() => {
  return props.isUser
    ? 'bg-blue-200 rounded-xl rounded-tr-none' // Blue for user messages, rounded except top-right
    : `${props.backgroundColor} rounded-xl rounded-tl-none`; // Use prop for agent messages, rounded except top-left
});
</script>
