<template>
    <Hero :title="post.title" :image="post.image" />
</template>

<script>
import Hero from '@/components/Hero.vue'

export default {
    name: 'BlogPost',
    components: {
        Hero,
    },
    props: {
        post: {
            type: Object,
            required: true,
        }
    },
}
</script>

