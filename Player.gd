extends CharacterBody2D

var key_counter = 0
var coin_counter = 0
@onready var key_label = $"../key/k_label"
@onready var _animated_sprite = $AnimatedSprite2D

func _process(_delta):
	if Input.is_action_pressed("ui_right"):
		_animated_sprite.play("run")
	elif Input.is_action_pressed("ui_left"):
		_animated_sprite.play("back")
	else:
		_animated_sprite.play("idle")
   
@onready var coin_label =%Label

const SPEED = 120.0
const JUMP_VELOCITY = -300.0


func _physics_process(delta: float) -> void:
	
	if not is_on_floor():
		velocity += get_gravity() * delta

	
	if Input.is_action_just_pressed("jump") and is_on_floor():
		velocity.y = JUMP_VELOCITY

	#
	var direction := Input.get_axis("move_left", "move_right")
	if direction:
		velocity.x = direction * SPEED
	else:
		velocity.x = move_toward(velocity.x, 0, SPEED)

	move_and_slide()



func set_coin(new_coin_count: int) -> void:
	coin_counter=new_coin_count
	coin_label.text = "Coin :" + str(coin_counter)


func _on_area_2d_area_entered(area: Area2D) -> void:
	if area.is_in_group("coin"):
		set_coin(coin_counter +1)
	elif area.is_in_group("key"):
		set_key(key_counter +1)

func set_key(new_kcount: int) -> void:
	key_counter=new_kcount
	print(key_counter)
	key_label.text = "Keys :" +str(key_counter)
	
