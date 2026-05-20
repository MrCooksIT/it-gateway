<script setup>
import { onMounted } from 'vue'

onMounted(() => {
  if (typeof window === 'undefined') return

  window.Tawk_API = window.Tawk_API || {}
  window.Tawk_LoadStart = new Date()

  const s1 = document.createElement('script')
  const s0 = document.getElementsByTagName('script')[0]
  s1.async = true
  s1.src = 'https://embed.tawk.to/6a0d761769cc591c36969fef/1jp29ajfs'
  s1.charset = 'UTF-8'
  s1.setAttribute('crossorigin', '*')
  s0.parentNode.insertBefore(s1, s0)
})
</script>

<template>
  <div />
</template>
