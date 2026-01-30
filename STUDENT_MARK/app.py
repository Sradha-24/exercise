from flask import Flask,request,jsonify

app=Flask(__name__)
students=[
       {"id":1,
           "name":"Rahul",
     "marks":40}
] 



@app.route('/')
def base():
    return("start")

@app.route('/student/add',methods=['POST','GET'])
def add_student():
    data=request.get_json()

    if not data or 'name' not in data  or 'marks' not in data:
        return jsonify({"error":"Missing name or marks"}),400
    
    if data['marks']>100:
        return jsonify({"message":"marks should be leass than 100"})
    new_student={
        "id":len(students)+1,
        "name":data['name'],
        "marks":data['marks']
    }
    students.append(new_student)
    return jsonify(new_student),201

@app.route('/student/get',methods=['GET'])
def get_student():
   return jsonify({"students":students}),200

@app.route('/student/get/<int:id>',methods=['GET','POST'])
def get_one_student(id):
    for i in students:
        if i.get("id") == id:
           print(i.get('id'))
           return jsonify({"students":i}),200
    return jsonify({"message":"Not found"}),404

@app.route('/student/update/<int:id>',methods=['PUT'])
def update_student(id):
    data=request.get_json()
    for i in students:
        if i.get('id')==id:
          if 'name' in data:
              i['name']=data['name']
          if 'marks' in data:
              i['marks']=data['marks']
    return jsonify({"message":"Updated"})
@app.route('/student/delete/<int:id>',methods=['DELETE'])
def delete_student(id):
    for x,i in enumerate(students):
        if i.get('id')==id:
           students.pop(x)
           return jsonify({"message":"deleted succesfully"})
    return jsonify({"message":"id not found"})

if __name__=='__main__':
    app.run(debug=True)