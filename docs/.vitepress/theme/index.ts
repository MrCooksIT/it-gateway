import DefaultTheme from 'vitepress/theme'
import HelpButton from './HelpButton.vue'
import { h } from 'vue'
import './custom.css'

export default {
  extends: DefaultTheme,
  Layout() {
    return h(DefaultTheme.Layout, null, {
      'layout-bottom': () => h(HelpButton),
    })
  },
}
