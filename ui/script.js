var api_url = "http://127.0.0.1:8000";
var app = new Vue({
	el: '#app',
	data: {
		user: {},
		answers: {},
		currentAnswer: {},
		answerEditFormShow: false,

	},
	created: function () {
		
	},
	computed: {
		missingName: function () { 
			return false;
		}
	},
	methods: {
		changeState: function(state){
			this.state = state;
		},
		login: function(){
			var scope =  this;
			var xhr = new XMLHttpRequest();
			xhr.open("POST", api_url + '/api/auth-token/', true);
			xhr.setRequestHeader("Content-type", "application/json");
			xhr.setRequestHeader("Access-Control-Allow-Origin","*");
			xhr.onreadystatechange = function() {
			    if(xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
			        scope.user = JSON.parse(xhr.response);
			        scope.getAnswer();
			    }
			}
			xhr.send(JSON.stringify(this.user)); 
		},
		logout: function(){
			this.user = {};
		},
		getAnswer: function(){
			var scope =  this;
			var xhr = new XMLHttpRequest();
			xhr.open("GET", api_url + '/api/answer/', true);
			xhr.setRequestHeader("Content-type", "application/json");
			xhr.setRequestHeader("Access-Control-Allow-Origin","*");
			xhr.setRequestHeader("Authorization","Token " + scope.user.token);

			xhr.onreadystatechange = function() {
			    if(xhr.readyState == XMLHttpRequest.DONE && xhr.status == 200) {
			        scope.answers = JSON.parse(xhr.response);
			        if (scope.answers.length == 0) 
			        	scope.answerEditFormShow = true;
			        else
			        	scope.answerEditFormShow = false;
			    }
			}
			xhr.send(); 
		},
		save: function() {
			var scope =  this;
			var xhr = new XMLHttpRequest();
			if (scope.currentAnswer.id) 
				xhr.open("PUT", api_url + '/api/answer/' + scope.currentAnswer.id + '/', true);
			else
				xhr.open("POST", api_url + '/api/answer/', true);
			xhr.setRequestHeader("Content-type", "application/json");
			xhr.setRequestHeader("Access-Control-Allow-Origin","*");
			xhr.setRequestHeader("Authorization","Token " + scope.user.token);
			xhr.onreadystatechange = function() {
			    if(xhr.readyState == XMLHttpRequest.DONE) {
			        console.log(xhr.response);
			        scope.getAnswer();
			        scope.currentAnswer = {};
			    }
			}
			xhr.send(JSON.stringify(this.currentAnswer));
		},
		editAnswer: function(answer){
			this.answerEditFormShow = true;
			this.currentAnswer = Object.assign({}, answer);
		},
		deleteAnswer: function(answer) {
			var scope =  this;
			var xhr = new XMLHttpRequest();
			
			xhr.open("DELETE", api_url + '/api/answer/' + answer.id + '/', true);
			xhr.setRequestHeader("Content-type", "application/json");
			xhr.setRequestHeader("Access-Control-Allow-Origin","*");
			xhr.setRequestHeader("Authorization","Token " + scope.user.token);
			xhr.onreadystatechange = function() {
			    if(xhr.readyState == XMLHttpRequest.DONE) {
			        console.log(xhr.response);
			        scope.getAnswer();
			    }
			}
			xhr.send();
		},
		register: function(){
			var scope =  this;
			var xhr = new XMLHttpRequest();
			xhr.open("POST", api_url + '/api/user_create/', true);
			xhr.setRequestHeader("Content-type", "application/json");
			xhr.setRequestHeader("Access-Control-Allow-Origin","*");
			xhr.onreadystatechange = function() {
			    if(xhr.readyState == XMLHttpRequest.DONE) {
			    	console.log(xhr.response)
			    	if (xhr.status == 400) 
			    		alert("Error: " + xhr.response)
			    	if (xhr.status == 200) 
			    		alert("Registration done, try to login")
			    }
			}
			xhr.send(JSON.stringify({username: this.user.username, email: this.user.username, password: this.user.password}));
		}
	}
})