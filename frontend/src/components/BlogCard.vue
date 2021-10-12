<template>
    <router-link :to="{ name: 'BlogPost', params: {id: post.id} }">
        <div class="blog-card">
            <h3>{{ post.title }}</h3>
            <p>{{ post.body.split(" ").slice(0, 10) }}...</p>
        </div>
    </router-link>
</template>

<script>
export default {
    name: 'BlogCard',
    props: {
        post,
    },
}
</script>