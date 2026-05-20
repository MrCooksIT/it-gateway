import DefaultTheme from 'vitepress/theme'
import TawkTo from './TawkTo.vue'
import { h } from 'vue'

export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      'layout-bottom': () => h(TawkTo),
    })
  },
}
