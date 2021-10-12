<template>
    <div class="blog-carousel">
    <router-link :to="{ name: 'BlogPost' }">
        <div v-for="(post, index) in posts" :key="index" class="blog-card">
            <h3>{{ post.title }}</h3>
            <p>{{ post.snippet }}</p>
        </div>
    </router-link>
    </div>
</template>

<script>
export default {
    name: 'BlogCarousel',
}
</script>