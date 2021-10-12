<template>
  <footer>
    <ul v-if="socialLinks" class="social-links">
      <li v-for="(socialLink, index) in socialLinks" :key="index">
        <a :href="socialLink.url">{{ socialLink.platform }}</a>
      </li>
    </ul>
    <div class="copyright">
      &copy; {{ copyright.company }} {{ copyright.year }}
    </div>
  </footer>
</template>

<script>
export default {
  name: 'Footer',
  props: {
    copyright: {
        type: Object,
        default() {
            return {
                company: 'Example Company',
                year: 2021,
            }
        }
    },
    socialLinks: Array,
  },
};
</script>

<style scoped>
footer {
  background-color: black;
  color: white;
}

.copyright {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 40px;
  color: grey;
}
</style>