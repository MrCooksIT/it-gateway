<script setup>
// "Ask Mr Coetzee" help button.
// The chat service (tawk.to) is NOT loaded with the page. Its script is only
// fetched when a learner clicks this button, so learners who never ask for
// help are never tracked and never see a chat bubble or pop-up.
import { ref } from 'vue'

const TAWK_SRC = 'https://embed.tawk.to/6a0d761769cc591c36969fef/1jp29ajfs'

// idle: only our button shows · loading: script is being fetched
// open: the chat window is showing · failed: the script could not load
const state = ref('idle')
// true when Mr Coetzee has replied while the chat window is closed
const unread = ref(false)
let scriptAdded = false

function openChat() {
  const api = window.Tawk_API
  if (api && typeof api.showWidget === 'function') {
    api.showWidget()
    api.maximize()
    state.value = 'open'
    unread.value = false
  }
}

function askForHelp() {
  if (typeof window === 'undefined') return

  // Already loaded earlier in this visit: just open it again.
  if (scriptAdded && state.value !== 'failed') {
    openChat()
    return
  }

  state.value = 'loading'
  window.Tawk_API = window.Tawk_API || {}
  window.Tawk_LoadStart = new Date()

  // Open the chat as soon as it is ready.
  window.Tawk_API.onLoad = openChat

  // When the learner closes the chat, remove tawk.to's own bubble again
  // so that only our quiet button is left on the page.
  window.Tawk_API.onChatMinimized = () => {
    window.Tawk_API.hideWidget()
    state.value = 'idle'
  }

  // A reply that arrives while the chat is closed shows on our button.
  window.Tawk_API.onUnreadCountChanged = (count) => {
    unread.value = count > 0 && state.value !== 'open'
  }

  const s = document.createElement('script')
  s.async = true
  s.src = TAWK_SRC
  s.charset = 'UTF-8'
  s.setAttribute('crossorigin', '*')
  s.onerror = () => {
    scriptAdded = false
    state.value = 'failed'
  }
  document.head.appendChild(s)
  scriptAdded = true
}
</script>

<template>
  <div v-if="state !== 'open'" class="itg-help">
    <p v-if="state === 'failed'" class="itg-help-note" role="status">
      The chat could not load. Check your connection and try again.
    </p>
    <button
      type="button"
      class="itg-help-btn"
      :disabled="state === 'loading'"
      @click="askForHelp"
    >
      <svg class="itg-help-icon" viewBox="0 0 24 24" aria-hidden="true">
        <path
          d="M4 5.5A2.5 2.5 0 0 1 6.5 3h11A2.5 2.5 0 0 1 20 5.5v8a2.5 2.5 0 0 1-2.5 2.5H11l-4.4 3.6c-.5.4-1.1 0-1.1-.6V16A2.5 2.5 0 0 1 4 13.5z"
          fill="none"
          stroke="currentColor"
          stroke-width="1.8"
          stroke-linejoin="round"
        />
      </svg>
      <span v-if="state === 'loading'">Opening chat…</span>
      <span v-else-if="unread">New reply from Mr Coetzee</span>
      <span v-else>Ask Mr Coetzee</span>
      <span v-if="unread" class="itg-help-dot" aria-hidden="true"></span>
    </button>
  </div>
</template>

<style scoped>
.itg-help {
  position: fixed;
  right: 1rem;
  bottom: 1rem;
  z-index: 40;
  display: flex;
  flex-direction: column;
  align-items: flex-end;
  gap: 0.4rem;
}

.itg-help-btn {
  display: inline-flex;
  align-items: center;
  gap: 0.45rem;
  padding: 0.5rem 0.85rem;
  border: 1px solid var(--vp-c-brand-1);
  border-radius: 999px;
  background: var(--vp-c-bg-elv);
  color: var(--vp-c-brand-1);
  font-size: 0.85rem;
  font-weight: 600;
  line-height: 1;
  cursor: pointer;
  box-shadow: var(--vp-shadow-2);
  transition: background-color 0.15s, color 0.15s;
}

.itg-help-btn:hover:not(:disabled),
.itg-help-btn:focus-visible {
  background: var(--vp-c-brand-1);
  color: var(--vp-c-bg);
}

.itg-help-btn:focus-visible {
  outline: 2px solid var(--vp-c-brand-1);
  outline-offset: 2px;
}

.itg-help-btn:disabled {
  cursor: progress;
  opacity: 0.75;
}

.itg-help-icon {
  width: 1.05rem;
  height: 1.05rem;
  flex: none;
}

.itg-help-dot {
  width: 0.55rem;
  height: 0.55rem;
  border-radius: 50%;
  background: var(--vp-c-danger-1);
  flex: none;
}

.itg-help-note {
  max-width: 15rem;
  margin: 0;
  padding: 0.45rem 0.65rem;
  border-radius: 8px;
  background: var(--vp-c-bg-elv);
  border: 1px solid var(--vp-c-divider);
  color: var(--vp-c-text-1);
  font-size: 0.78rem;
  line-height: 1.35;
  box-shadow: var(--vp-shadow-2);
}

@media print {
  .itg-help {
    display: none;
  }
}
</style>
