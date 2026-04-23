SIG: Arrow SIG
Date: 2026-04-22
Duration: 44 minutes
============================================================

## Zoom Recording Transcript

**Albert Lockett** 00:31 Hey, Mike?
**Mike "Blanch" Blanchard** 00:34 Hey, Albert!
**Albert Lockett** 00:36 How's it going?
**Mike "Blanch" Blanchard** 00:36 Good. How you doing?
**Albert Lockett** 00:39 Yeah, pretty good. Enjoying, earth Day… Yeah, I don't know how I'm enjoying it, but I guess… Mike "Blanch" Blanchard 00:48 You could cook.
**Albert Lockett** 00:49 Working on query engine stuff is… Not really related at all, so, Yeah, so, what's up? Did you have anything, to discuss this week?
**Mike "Blanch" Blanchard** 01:01 Nothing in particular, no.
**Albert Lockett** 01:04 Okay, cool. Yeah, I had… I had one thing, if you've got a few minutes.
**Mike "Blanch" Blanchard** 01:08 Sure.
**Albert Lockett** 01:08 Okay, let me share… I'll go to the, GitHub, and I'll make it… make my screen bigger. Am I sharing? Yeah, I think I… okay, I managed to get it to share.
So… And this is, like, this isn't, like, super pressing, so, we had to discuss it now, or we could, you know, save it for later. Like, let me know, like, if you have to go over anything.
But if you have a few minutes, we can talk about it.
So… do you have a few minutes?
**Mike "Blanch" Blanchard** 01:48 Yeah.
**Albert Lockett** 01:48 Okay, awesome.
Yeah, so I wanted to talk about, this issue here. So… Basically, when I, like, so… when we, have a function that we're defining, We define it, it seems like, as a list of, a list of parameters. So we've got our, like, our function definition. It has a list of parameters, and each parameter, has a, has a type, which I think is an enum.
If I go to a here… Function parameter type, It's an enum. Yeah, it's… so it's a scaler, that can, that can be a, A value, or it can be, a mutable value.
And then, And then when we add, like, say we add a new function or add a new external function, we give it… the, the function, and then we give it, parameter names, and then we give it, default values, or if it's, if it's an external function, then, Then, like, when we're adding it to, like, our parser state, like, making it available, we just give it the name and the, and the list of, like, name parameters.
And so, what I was thinking here was that, This is, this is, like, this, this works really good when, like, we know exactly, like, what the, what the parameters are going to be. But I was thinking that, like, there might be cases where we have a function that we're trying to add that has, like.
**either a variable number of parameters, so, like, some of the parameters at the end could be optional, and, like, you don't have to pass them, or… Mike "Blanch" Blanchard** 03:55 default values are for?
**Albert Lockett** 03:58 But, yeah, but then, I guess I was… okay, so, so… Yeah, so I had, so I had two, so I had.
**Mike "Blanch" Blanchard** 04:08 If you have a default value defined, and you don't specify a parameter, then it just gets set to the default.
**Albert Lockett** 04:16 Yeah, so I guess, like, what I was thinking was, like, like, what if there was a, like, a function, like, that, that, That we were going to use that, like, was written in such a way that, it already had, like, internally, like, some default parameters. So let's say, like.
like, I'm thinking of, like, the… some of, like, the data fusion functions that we might use for things like, like, regex matching or, you know, some of, like, the data fusion functions we looked at last week. Those can… the way they define the signature, is that you can create a signature with, like, a variable number of arguments and say.
Say it would, like… let's say it's, like, substring, right? So you pass, like, the string, and then you pass either a start, or you pass a start and an end, right? So you're, like, getting a range from the string. Maybe internally, that third parameter it says, okay, if I don't… if I don't receive this, then I'm just going to, like, use a default, which is, like, the… the, the length of the string, right? So, like… substring is, like, an example where the default parameter is, like, computed based on the argument that, like, you passed in at the… at the start.
**Mike "Blanch" Blanchard** 05:54 Just set the default value to null , and then just check.
**Albert Lockett** 05:59 Okay, yeah, sure, I guess, but, like, okay, but here, like, so let me, let me, you know, give another example, like, what if, what if we, what if we said, yeah, so we could do that, I guess.
I guess, like, so what if, the other kind of, like, concern I had, just on… on this, was, like, what if… like, internally to your function, what if it, like, already, like, had its results? What if it said, hey, you know what, if I get two parameters, then I know that, like, the default value for my third parameter is defined, like.
internally, right? So it's like, now, if we want to, like, if we want to, like, use that function, now we've got our default parameters kind of, like, defined in two places. We've got them defined internally to the function, and we've got them defined, like, externally in this, in this, In the function parameter in our parser state, which seemed, which seems, like, redundant. Now, I guess it's not so bad, you know, it's not the end of the world if you have those optional parameters kind of, like, set up in two places, but… But… so that was, like, one thing I was trying to, like, maybe avoid. The other… the other thing, Was, like, what if you had… a function that you wanted to call that took, like, a variable number of parameters. So, I was thinking, like, if it, like, concat would be an example. I know we have, like, concatenate strings in our, in our, in our function tree, but, like, what if you wanted to write a function that worked like concat, that just took some arbitrary number of strings and then said, okay, I'm gonna, like, slam them together, Like, we don't really have a way to, like, define, like, a func… like, have a function that we define the signature that says, hey, this can take any number of parameters.
**So, I guess, like… what I… what I was gonna try to propose, was, like… Mike "Blanch" Blanchard** 08:20 So you just pass in an array or a list.
**Albert Lockett** 08:24 Okay, yeah, sure, we can… we can do that too.
Yeah, look, if, like, if, if, if, if, if, if, you're not thinking that, like, we need to worry about this, then I won't, like, go into the solutions. I guess, like.
**Mike "Blanch" Blanchard** 08:44 I mean, that sounds… That's how it works today in the parser and the expression tree, if you go look at, like, CONCAT.
the expression… It probably just takes a scalar, so you can give it… anything, but if you go look at the parser, what it will do is, like, if it sees one argument, or 10, It will just… Create an inner thing, which is create a list.
So it will go evaluate, if you give it 10 things, it'll evaluate them all, and then it'll pass it essentially as an array.
**Albert Lockett** 09:24 Yeah, okay.
**Mike "Blanch" Blanchard** 09:26 I'm sure my blood work.
probably what, like, the C-sharp compiler does in both of these cases, like, optional parameters and… C-sharp, it's just compiler magic.
Which is really the same thing that happens here, is like… when it's parsing, when it's compiling that function invocation, it looks at the definition and says, okay, I was expecting 5 things, user only gave me 3, But I have two defaults, so it just puts them… puts them at the call site as though the user passed them.
**Albert Lockett** 10:03 Yeah, okay. Yeah, sure.
Okay.
Yeah, sure.
**Mike "Blanch" Blanchard** 10:16 I should have some tests in there, too, if you go look at, like, the KQL stuff. I should have some optional parameter tests in there to make sure…
**Albert Lockett** 10:25 Yeah?
Okay, like, if you know where they are offhand, we can go… I can go, try to look at them. I guess, like, So… so you're not thinking, like, there would ever be a case where, like, You would have, like… Like, an external function, let's say, that could take some variable number of, of parameters. And, And in your, like… In your parser, you're gonna say, like.
**okay, if I get two parameters, and let's say there's an optional third one, Like, I'm just gonna… like, I guess, like, the thing is, like, you have, like, you have no way to know, based on, like, your, your, your signature that you get from the… from the, from the parser state to say, hey, well, I got two parameters there's, like… Mike "Blanch" Blanchard** 11:30 I don't think it's really needed, so we have the same thing in C-sharp, there's, like, a params keyword.
So you can define a function and say, okay, it takes an int ID, a string name, and then params. And you can dump whatever you want.
However many you want.
But it's just compiler magic. What ends up happening is you get an array.
And you can do the same thing here, you just define your pests so that… You know, your pest rule has a comma, optional, you know, star.
So in your parser, you can handle… okay, a user can give me… there's a couple fixed positions, and then they can chain whatever they want. And then as you're parsing that, you just pass it as an array.
And you define the last argument as this is just gonna be an array of things.
**Albert Lockett** 12:23 I know.
E… okay.
**Mike "Blanch" Blanchard** 12:32 even goal here can count.
It should be doing that already.
**Albert Lockett** 12:41 Yeah, so, okay, yeah, yeah, so, okay, but, like, so, okay, you know what, like, I'm, like, if you think that, like, we don't need to change this, I'm not gonna, like, I'm not gonna, like, spend much time arguing, but I just think that, like, you know, from my perspective, right, so, like.
I… I might come in and say, hey, you know, I want to call some… I have some… I have some function I want to call. It's a data fusion scalar function. In those scalar functions.
they can have… they can take a variable number of parameters. Their… their… their signature is not just, it's… it's this fixed number of parameters. It's… you can pass it some number of parameters, and then it will figure out, okay, you know what, if it's passed with 2, I have… internally, I know there's a default of 3 or something, right, that I could use. But, like.
So the issue I have is, like.
I… so if I was gonna say, okay, I'm gonna add one of those functions to my parser scope as, as a function that, like, could be called an OPL, I don't have a way to, like, say, okay, like, this… like, this named function is something I've parsed. I have a function, that I can get from the parser scope by that name. I get the function definition from the parser scope, and then I see okay, it takes 3 parameters. Even though the actual implementation of that function, when I go to call it.
could use two parameters, or four parameters, right? It can take, like, it has a… it has a signature that is, that is variable. So now what I have to do is I have to fill in, like, basically all the, default parameters even though that function definition might have already defined those default parameters internally. And so, like, I guess what I was trying to… maybe suggest here would be that, like, is there a way that we could change how the, how the function signature manages parameters that would… that would maybe make that, like, a bit easier for me to work with.
But if, if, if, if, if you're not thinking that, like, that's something we need to do, then I can just, I can try to figure out a way to live with it.
**Mike "Blanch" Blanchard** 15:03 I mean, I'm open to doing anything, I just don't see the need, and I don't… If you dug into Rust… like, it's giving you what looks like something that can take in arbitrary numbers, but I doubt in the compiled binary, that's the case. Like, the computer just needs to know. It's gonna push a certain number of things to the stack, and manage the pointers, and…
**Albert Lockett** 15:27 So, okay, but no, so, so let me, let me, let me, let me back up here, because it's not, like, a Rust function that I'm calling, necessarily. It would be, like, like, if I go look at, so if I go look at, like, the, the… the… like, the… the trait for, like, a data fusion scalar expression, or scalar function implementation here.
Let me find one that I wrote… Regex, substir, substring… So, you can see that what it has here is you pass it like this, this argument… and then it has a vec of column values, and these column values are either going to be an array or a… or a scalar, right? So the way that, like… so you just, like, you basically get yourself, A vec of, of arguments, every time.
But then, in your, and your signature here… you can either say, like, this is going to be, like, a fixed number of arguments that I receive, or it's going to be, like, a variable number of arguments I receive, right? So, like, if I'm in the OPL query engine, and I'm, like, invoking this function, then yeah, I can just take, like, all the arguments that, like, that were passed from parsing and, like, you know, stick them into that vec and go invoke this function.
But the… but, like, as I'm… when I'm parsing.
I don't have a way to, to say, like, hey, here's this external function that's available, and by the way, it's sig… like, the signature, it can take two arguments, or it can take three arguments. I, like… it's… it's because… because our… because in our… in our AST, the number of parameters that we have to the function is… is… It's always fixed, or we have to define the, the… the… The… the default values ahead of time, versus, like.
like, how… like, some of these functions are written, like, the default values might be, like… it might have a default value that it can… it knows internally, so it seemed like maybe I wouldn't want to also have to, you know, define them in the parser.
**Mike "Blanch" Blanchard** 18:09 I, .
**Albert Lockett** 18:18 So… Mike "Blanch" Blanchard 18:19 Strong need here to make a change.
Because you can always just give it one parameter, which is just an array.
**Albert Lockett** 18:31 Okay, yeah, sure, so, I, Okay, so… So you don't think, like… okay, so, so, so, let me… So let me… Let me… Back up here. If… Okay, so let me… let me… let me back up here and just… just make sure that, like, that I'm not… that I'm not missing something, because if you don't see the need. So, let's say I'm parsing, let's say I'm parsing a function call, my… so I get some expression that calls some function, it's got… some arguments. And then, as my parser state is going along from the parser state, I'm gonna try to get, like, the definition of… of, of my… okay, so let's… okay, let's back up here for a sec. I know that when I go to, execute, my func.
Internally in my engine, I might… I'm gonna end up building something like args equals… A, B, right? I know these will be, like, scalar expressions, but let's say for the sake of argument that, like, Shoot, what am I doing here?
I don't know why the Python thing is opening.
So I'm gonna have a VEC of… of args, and then I'm gonna pass them to some… my func import.
ARGs… And then it's gonna spit me out an arrow array. Right, so this is in, like, in… In execution, this is the… Exper… I'm parsing.
And let's say that, like, this function could, like, you know, if it's two args, it can execute. If it had a third arg, it would also, like, know how to do the right thing.
So, when I'm parsing, I can get, like, my function definition from my parser state, and then I can get the parameters from that function definition.
And I… and in this case, I would, like… like, I think what I'd like to be able to do in the parser is… is what the KQL parser does, right? It can check, like, oh, you've passed two parameters, but this function expects 3, and so that's the wrong thing to do, and so I'm gonna, like, it's gonna be a parser error.
**But, like… Mike "Blanch" Blanchard** 21:31 Can you clarify your goal with this method? Are you trying… To have default optional parameters, or are you trying to allow a list of Any number of people.
**Albert Lockett** 21:44 I'm trying to have a way in my parser to verify that if I have a function implementation that can take some default, or some variable number of parameters, that I can when I… when I parse how many arguments were passed to the function that I'm going to… that I'm going to eventually invoke.
based on my expression, I'm trying to be able to validate that the… the number of parameters that I've passed is correct for the function that I'll eventually call.
**Mike "Blanch" Blanchard** 22:21 If you know the number of parameters, it doesn't sound like it's a variable.
Is that the case of optional parameters?
**Albert Lockett** 22:30 If I, so, Yeah, so, I mean, like, I guess, like… Sorry, if I know… sorry, if I know the number… sorry, I'm just trying to make sure I understand your question. If I know the number of parameters, it doesn't sound like it's optional, or it doesn't sound like it's variable. Okay, so, like, I… so I know how many functioners we have.
**Mike "Blanch" Blanchard** 22:54 You know there's, like, one required, and there's two optional.
You should be able to express that today, and you'll get all the validation Should already all be there.
**Albert Lockett** 23:04 Oh, yeah, okay, but, like, we don't have a way to say that, like, a, a parameter is optional, right?
**Mike "Blanch" Blanchard** 23:14 Law value, that makes it optional.
**Albert Lockett** 23:16 you give it a default value. Yeah, but I guess, like, what I was thinking was, like, like… if… If this… so… Okay, but like… like, what if… what if this… this… this function that I'm… that I'm calling, like.
it… it has, like, its own definition for, like, what it thinks the default value should be, right, internally, for some reason. Let's say… let's say that that was the case.
should… like, what do I define the default?
value as out here if I'm not actually going to end up, like, passing it when I call the function.
**Mike "Blanch" Blanchard** 24:01 I don't know if I've tried it, but tried it to give it a default of just null .
**Albert Lockett** 24:07 Yeah.
**Mike "Blanch" Blanchard** 24:08 see if it works, and then you can just detect, okay, if I have a value, the user did something. If I have a null , then I just put in my Whatever.
**Albert Lockett** 24:18 Okay, yeah, we could do that.
I guess I was thinking, like, it might be, Yeah, okay, yeah, we could do that. I'm wondering if it… like… Yeah, we could do that, okay. I guess, I guess, like, where I was going with this was, like, maybe it would make sense to try to be more explicit, like, if, If you could, like… Say, like.
you know, this… this… this function, like, maybe if there was, like, a flag on pipeline function parameters that was, like, this is an optional parameter or something, right? Versus, like, having to define a default value, and, like, the presence of the default value being, like, the indicator that it's an optional parameter.
**Mike "Blanch" Blanchard** 25:11 I wouldn't want to add… Another flag, but if you want to add, like, a helper method.
You know, just add some function, new optional, and just have it know how to construct things correctly.
**Albert Lockett** 25:29 Okay, and you wouldn't… okay, so… I can try that at a default… a default of, of null . I can try that.
**Mike "Blanch" Blanchard** 25:47 If it works, and if it doesn't work, then we'll have to make some change, and we can… Like, if you want… there's not a lot using this right now, so if you want… Like, if you want it… right now, there's just default values.
Yeah. There's a reason… there's a reason the names of the parameters and the default values are on the parser and not in the tree. So, like, when it comes to the tree.
the names are erased, and everything is invoked by IDs.
So that… might make it trickier, but if on the parser state structure.
If you wanted to, like, remove default values and put a structure there, like, optional values, and be able to set, you know, these ones are optional, these ones are optional with defaults.
I don't have an issue with that, if you want to just… Tweak it a little bit.
**Albert Lockett** 26:52 Yeah, sure. I mean, that's kind of, like, what I was… that was, like, the discussion that I was going to try to have, right? Would be, like… like, is it okay to tweak that? So you're thinking that, like, the way… like, the place it should be tweaked should be in the parser state.
And not in the… not in the, expression tree here. I mean, I'm okay with that.
**Mike "Blanch" Blanchard** 27:10 You think you could, because… When it comes to the final tree.
there's no such thing as, like, optional, so what'll end up in the tree is an invocation with the parameters just set. They're, like, fixed, like, okay, I'm still calling the function. Even though the user only gave me one argument, I'm invoking the function with three. I've just put in those defaults.
**Albert Lockett** 27:37 Right, right, right, right. Yeah, gotcha, gotcha. So it's gotta be in the, so it's gotta be in the parser state, effectively.
**Mike "Blanch" Blanchard** 27:44 Well, that's all the world of the parser.
The part job is to say, okay, user is invoking a function, I have the name, I have these two parameters with names, so now I go look at the definition, okay, I found it by name, cool, I have the ID, Now I look at the parameters, oh, this thing has 3, I only got 2, so now I'm gonna add the third one with the default value, and at that point, you could say, oh, this is an optional one with no value, I'm just gonna put in a null , so that you don't have to go and explicitly say, here's the default null , you could just make that more magical.
**Albert Lockett** 28:21 Yeah. Okay. Yeah, okay.
**Okay. Yeah, so this, so this is… Mike "Blanch" Blanchard** 28:30 You could even, like, a real simple thing to do would be on that parser state change on line 77 in that hash map.
You could just make that scalar expression an option.
**Albert Lockett** 28:43 Yeah.
**Mike "Blanch" Blanchard** 28:44 A little clunky, but…
**Albert Lockett** 28:46 Yeah.
**Mike "Blanch" Blanchard** 28:48 basically say, okay, I'm declaring some parameter as an optional without a default value.
it might make more sense. If you are going to do that, make that scalar option. Instead of calling the thing default values, call it optional parameters or something.
**Albert Lockett** 29:06 Yeah. Yeah, and then I guess, I guess you would need to, Somehow… maybe have some, like, some validation that, like, all your… All your optional parameters are, like, at the end of your… Mike "Blanch" Blanchard 29:26 That should…
**Albert Lockett** 29:27 any cable.
**Mike "Blanch" Blanchard** 29:27 I'm pretty sure I wrote those tests, because, like.
KQL has the same rules, like, if you're invoking a function.
The second you, like, name a parameter or get funky, then the order is important.
So that should be there… I'll try to dig out where those tests are so you can go see, but… it should… that should be there. Like, if you give it a parameter with the wrong name, it should tell you. If you give it too many parameters, it should tell you. If you're missing something without a default, it should tell you. If you do some funky order and it can't figure things out, it should tell you.
**Albert Lockett** 30:07 This is… this is when you invoke the function, or this is when you, like, push the function in the parser state?
**Mike "Blanch" Blanchard** 30:13 It should be part of the parser, yeah.
**Albert Lockett** 30:15 part of the parser, right, okay, okay, gotcha. Alright, yeah, cool, so that makes sense. So then I think, yeah, so it's just like, if we do want to do this, then, Then, yeah, it's like, we could… like, how we're managing these default values. We could somehow slightly change this type, to make it an indication that, like, more, more, like, make it more clear that, like.
how you define a parameter that doesn't… that is optional, that doesn't necessarily have a default that needs to be filled in by the parser.
**Mike "Blanch" Blanchard** 30:58 Do you want to just call that, you know, optional parameters, and then… Yeah. It's a struct, or if you just want to make that scalar an option.
Whatever.
Whatever you.
It's worth your time.
**Albert Lockett** 31:14 Yeah, okay.
**Mike "Blanch" Blanchard** 31:15 I can't imagine many people in the universe will ever work on this code. You know, me, you, maybe some others in the future, but it's gonna be a small set, so… There are.
**Albert Lockett** 31:25 Yeah.
**Mike "Blanch" Blanchard** 31:26 places where, like, I don't… I don't go nuts on making the most friendly API in history.
**Albert Lockett** 31:33 Yeah.
Okay, yeah, I think that's, I think that's… I think that's pretty reasonable, and then I'll just try to… if I do make that change, I'll just have to, like, I'll be trying to make sure that, like, we don't have, We're not, we're not having, any of the tests break, because like you said, there's quite a few tests that are.
**Mike "Blanch" Blanchard** 31:55 Yeah, try the null . There might be a line of code somewhere that says, like, oh, I don't have a value, I'm emitting an error, but you could loosen it if you want to make that valid.
**Albert Lockett** 32:06 Okay, okay, yeah, sounds good.
**Alright, yeah, that sounds like the easiest thing to do then, and then, for the VARG stuff, like you said, yeah, that could, I guess, I guess, that can just… Just, just, parse that into a, trying to… Mike "Blanch" Blanchard** 32:25 If it's… doesn't work…
**Albert Lockett** 32:27 programs.
**Mike "Blanch" Blanchard** 32:28 you know, prohibitive. Like, I'm open to changes, I just… off the… off the dome, I feel like you should be able to do it with just arrays, but, like, scroll up a little bit.
Do you have the pipeline function?
Where is it?
Pipeline function parameter type, what's that enum?
**Albert Lockett** 32:49 Yeah, let me see if I can find that. Pipeline function parameter type. This takes, it's an enum with a scalar and a mutable value. This is gonna be easier if I look at it in VS Code, probably.
**Mike "Blanch" Blanchard** 33:02 Good. I mean, if you really, really, really determine there's a need, you might be able to do something on that to just say.
Scalar variable or something.
**Albert Lockett** 33:14 Yeah, pipeline function parameter type, yeah, and then this has a… it's got an array in it, so you could… Yeah.
**Mike "Blanch" Blanchard** 33:25 You can definitely pass.
**Albert Lockett** 33:26 Hell yeah, I see what you mean.
**Mike "Blanch" Blanchard** 33:27 An array to a function all day long.
**Albert Lockett** 33:30 Yeah, what's that?
**Mike "Blanch" Blanchard** 33:31 You can definitely pass an array to a function.
**Albert Lockett** 33:34 Yeah.
Yeah.
Okay. Yeah, so I think that can… I think that, like, in… yeah, so you're right, in the worst case scenario, if, like, we do need to do… of our args thing, we could, at a, Add a variant to this, because this is, where is that used again?
Pipeline function parameter… Oh, right, okay, so, but then, okay, yeah, so then when you're parsing, like, you can get access to this pipeline function, because you've got the function ID, so you grab this… And then… and then you can look at the parameters, right? Right, right.
Okay, cool.
Yeah, that… okay, yeah, that seems like the most, Okay, so those… it seems like we've got our bases covered, then. In… in… you know… In a way that, like, if we did need to make modifications to support both of these.
We don't have to do anything, like, crazy. Okay.
Cool.
Okay.
Gotcha.
Okay, yeah, that's helpful to know that, like, if, like, the kind of optional stuff should be in the parser state, that's super helpful to know.
Yeah.
Cool.
Alright, yeah, that sounds good. That's, That's, that's… that's kind of, like, what I wanted to get out of the, out of the, out of the conversation, was just, like, a little bit of guidance on… on, like, if… if that change is going to be made, like, like, where it should be done.
And, and, and a little bit of guidance on how it should be done, and I think that… I think that that's, I think that's pretty much, where we landed.
Okay, cool.
Alright, yeah, and I don't know if I'll make that change, straight away, either. It was just something I was kind of, like, like, thinking about after, like, I remember, like, remember I said a couple weeks ago, I was, like.
Adding, like, some code in the OPL, or the, the… the OTAP, query engine that I was writing to call some functions, and so… as I was looking at the signature of those functions, I was trying to figure out, like, how do we, like… How do we, like, get the… get, like, alignment in the parser state with, like, what these, like, what these scalar function signatures are, How they're defined, basically.
Because Data Fusion is a really… much more… they do something a lot more complex than we do. Like, their signatures for the scalar functions are basically, like, Like, an enum that can take on… a bunch of different types. There's, like, there's, like… an enum for… pass anything you want, there's an enum for, like, pass these fixed number of parameters, there's an enum for, like, variable number of parameters, there's an enum that's, like, a one-of that can… you can combine different signatures together, right? And so… Anyway, I don't think we need to go that far with it, but I was just trying to figure out, like, okay, like, from… as I'm parsing, if I have a function that I know I need to pass like, these parameters into it, but it's kind of variable which ones could go into it. How do I define that? Or how do I know that from the parser state?
And I think I've got a path forward, if, If, I need to go there.
**Mike "Blanch" Blanchard** 37:24 Okay, sounds good.
**Albert Lockett** 37:26 Yeah Thanks a lot, thanks a lot.
**Mike "Blanch" Blanchard** 37:30 Sure, just ping me if you run into anything.
**Albert Lockett** 37:33 Of course, yeah.
And I think that's all I had this week.
I think that's all I had.
**Mike "Blanch" Blanchard** 37:42 Okay, sounds good.
**Albert Lockett** 37:46 Cool, Ann. Sorry, do you have anything else?
**Mike "Blanch" Blanchard** 37:50 No, not really. Still trying to get my code over to you.
It's in really good shape, but I'm like… I had my log model just have, like, severity text, severity number, and attributes.
So I'm like, I should add, like, you know, flags, and event name, and… I got to, you know, time Unix Nano, and I didn't have Data Fusion code for, like, the timestamp stuff, so I did that.
working on, like, the fixed size binary for trace ID and span ID.
But it's… it's hard.
**Albert Lockett** 38:26 really close.
**Mike "Blanch" Blanchard** 38:27 I'm hoping in the next few days to be able to share it with you.
**Albert Lockett** 38:32 That's awesome.
**Mike "Blanch" Blanchard** 38:33 And what you do with it is up to you. I'm just gonna send you, like, here's the branch, you can go take a peek if you want.
**Albert Lockett** 38:40 Oh, man, I'm, Dino always glad that some inspiration. Yeah, that'd be great.
**Yeah, and, like, I mean, look, like, yeah, take it as far as, like, as you want to take it, like, I'm, if it's a pain in the ass to support all those fields, like, I'm happy to look at it if it's just, like, a certain subset of fields as well. I know that, like, the body field is gonna… might be, like, a pain in the ass to support, because it… it works the same way, like, attributes, where… Mike "Blanch" Blanchard** 39:09 a to-do in my code. Do you know, you mentioned a few weeks ago that, like, there's a website I use, I've just had it perpetually open in a tab, but it's, like, the OTAP structure thing, and you said once that, like, it needs to be updated for body.
**Albert Lockett** 39:28 Oh, yeah. Yup.
Yeah, we haven't, yeah, that was the, this… the OTEP… Spec has, has a pic… sorry, do you want… do you want me to link you that? .
**Mike "Blanch" Blanchard** 39:50 No, I'm trying to find it, I think I…
**Albert Lockett** 39:51 Okay, I can, so… Mike "Blanch" Blanchard 39:55 It's fine, but I can figure it out just by looking at the objects, but…
**Albert Lockett** 40:00 Okay, that's good.
One of the, one of the guys on.
**Mike "Blanch" Blanchard** 40:05 Looks like something.
**Albert Lockett** 40:07 NF5 wrote a, wrote, like, a somewhat updated spec recently.
And so, like, in… in section, And so this, like, this what I just shared, is pretty up-to-date.
And like, in… you can see in section, in section 5.1, it has the log structure with all the fields, and, like, it calls out, like, body is a… is a struct, and, like, here's all the fields that are inside it, but… Again, that one's, like, it's a real pain to support, so you might want to skip it.
**Mike "Blanch" Blanchard** 40:54 So look at the other one I sent you.
**Albert Lockett** 40:57 Oh, yeah.
**Mike "Blanch" Blanchard** 40:59 a little different. The other thing I had was, like, a picture, but this looks like it's… This is the old style, because it doesn't… it doesn't say struct on this one.
**Albert Lockett** 41:09 Oh, yeah, so now… yeah, so now body is a… is a struct array.
And, like, like, those fields, stir int type… Bool, Bytes, Sir, those are all, Fields inside the struct array.
**Mike "Blanch" Blanchard** 41:27 Okay, I haven't… I haven't looked at a struct type yet, but… At some point, I'll… Slug through that.
**Albert Lockett** 41:38 Sounds good. Yeah, let me know if you, If you have any questions about it, I'm happy to… I'm happy to speak to it a little bit.
Cause, that was… that was one thing that I've been… I've been trying to work on adding to our… to the… to the OTAB engine this week is the ability to deal with, these, Is the ability to deal with log body?
as an NEVAL, like, as a, as, like, this, this any val- this struct that represents, like, the hotel any value, effectively.
And, yeah, so, like, basically, Basically, like, what we try to do is, like, Say, like, if, if, If we… if we, like, have the struct, and, like, we're trying to, like, Do some, some… comparison to it. Let's say you're, like, comparing a string to the… to the… to the struct, like, while you're filtering, then, like… like, I've had to, like, write all this… I'm actually working on it right now, like, I have to, like, write all this logic to be, like.
Okay, well, like, check the type field of the struct, is it… is it a string? And then get the… Get the string field from the struct, and then do the comparison against the string field. And then you kind of, like.
and together the Boolean arrays for, like, the type comparison plus the string comparison, and then, like, do all, like, the null handling and stuff as well.
But, yeah, anyway, so… suffice to say, like, if you have questions, like, if you step into this world of, like, dealing with the log body struct and have questions about it, I can try to answer it, because, I'm becoming familiar with it this week.
**Mike "Blanch" Blanchard** 43:40 Thanks, Angie.
**Albert Lockett** 43:42 No problem.
Cool.
**Mike "Blanch" Blanchard** 43:49 Alright, thanks, Albert. Enjoy Earth Day.
**Albert Lockett** 43:52 Oh man, yeah, hey, you too. I'll, yeah, happy Earth Day.
**Mike "Blanch" Blanchard** 43:57 Alright.
**Albert Lockett** 43:57 See you later. Bye.
