<template>
    <Hero :full="true">
        <h1>{{ project.title }}</h1>
    </Hero>
</template>

<script>
import data from '@/data.js'
import Hero from '@/components/Hero.vue'

export default {
    data() {
        return {
            project: data.projects.find(project => project.id == this.$route.params.id),
        }
    },
    components: {
        Hero,
    }
}
</script>
