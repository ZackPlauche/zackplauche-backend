<template>
    <a class="icon" target="blank" :href="url"><i :class="icon.class"></i></a>
</template>

<script>
export default {
    props: {
        type: {
            type: String,
            required: true,
        },

    },
    data() {
        return {
            platform: [
                {
                    name: 'Facebook',
                    class: 'fa facebook'
                },
                {
                    name: 'Instagram',
                    class: 'fa instagram',
                }
            ]
        }
    }
}
</script>