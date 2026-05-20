<script setup>
import { onMounted } from 'vue'

onMounted(() => {
  if (typeof window === 'undefined') return

  // Replace these two values with your Tawk.to property ID and widget ID
  // Find them at: tawk.to → Administration → Channels → Chat Widget → Direct Chat Link
  const PROPERTY_ID = '6a0d761769cc591c36969fef'
  const WIDGET_ID   = '1jp29ajfs'

  window.Tawk_API = window.Tawk_API || {}
  window.Tawk_LoadStart = new Date()

  const s1 = document.createElement('script')
  const s0 = document.getElementsByTagName('script')[0]
  s1.async = true
  s1.src = `https://embed.tawk.to/${PROPERTY_ID}/${WIDGET_ID}`
  s1.charset = 'UTF-8'
  s1.setAttribute('crossorigin', '*')
  s0.parentNode.insertBefore(s1, s0)
})
</script>

<template>
  <div />
</template>
