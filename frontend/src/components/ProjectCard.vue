<template>
    <router-link style="text-decoration: none" :to="{ name: 'Project', params: { id: project.id, project: project, } }">
        <div class="project-card">
            <img class="background-image" :src="project.thumbnail">
            <div class="project-card-text">
                <h3 class="project-card-title">{{ project.title }}</h3>
                <p class="project-card-description" v-if="project.description">{{ project.description }}</p>
            </div>
        </div>
    </router-link>
</template>

<script>
    export default {
        name: 'ProjectCard',
        props: {
            project: {
                type: Object,
                required: true,
            },
        },
    };
</script>

<style lang="scss" scoped>
    .project-card {
        height: 250px;
        width: 400px;
        overflow: hidden;
        color: white;
        border-radius: 10px;
        position: relative;
        transition: transform .4s ease, background-color .4s ease;
        
        &:hover {
            background-color: #0003;
        }
        &:hover img { transform: scale(1.1); }
        
        img {
            position: absolute;
            height: 100%;
            width: 100%;
            top: 0;
            z-index: -1;
            transition: transform .4s ease;
            will-change: transform;
            pointer-events: none;
        }

        &-text {
            display: flex;
            align-items: flex-end;
            height: 100%;
            padding: 20px;
        }

        h3 {
            color: white;
            font-size: 28px;
        }    
        
        p {color: white;}
        
    }
</style>