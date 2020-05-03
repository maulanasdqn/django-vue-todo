function sendRequest(url, method, data){
    var r = axios({
        method: method,
        url: url,
        data: data,
        xsrfCookieName: 'csrftoken',
        xsrfHeaderName: 'X-CSRFToken',
        headers: {
            'X-Requested-with': 'XMLHttpRequest'
        }
    })
    return r
}

var app = new Vue({
    el: '#app',
    data: {
        task: '',
        tasks: [
            {judul: 'Satu'},
            {judul: 'Dua' }
        ]
    },
    created(){
        var vm = this;
        var r = sendRequest('','get')
            .then(function(response){
               vm.tasks = response.data.tasks;
            })
    },
    computed: {
        taskList(){
            function compare(a, b){
                if(a.completed > b.completed){
                    return 1;
                }
                if(a.completed < b.completed){
                    return 1;
                }
                return 0;
            }
            return this.tasks.sort(compare)
        }
    },
    methods: {
        buatTask(){
            var vm = this;
            var fD = new FormData();
            fD.append('judul', this.task);

            sendRequest('','post',fD)
                .then(function(response){
                    vm.tasks.push(response.data.task);
                    vm.task = '';
                })

        },
        beres(id, index){
            var vm = this;
            sendRequest('' + id + '/beres/', 'post')
                .then(function(response){
                    vm.tasks.splice(index, 1);
                    vm.tasks.push(response.data.task);

                })
        },
        hapus(id, index){
            var vm = this;
            sendRequest('' + id + '/hapus/', 'post')
                .then(function(response){
                    vm.tasks.splice(index, 1);
                })
        }
    }

 })
