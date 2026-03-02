SIG: Event WG
Date: 2025-09-02
Duration: 59 minutes
Zoom Recording URL: https://zoom.us/rec/share/K_u1k69eUtJbbRZkZBaB_5eJVPzbztNeFN3sxaejLTYQ5RwsUJ8IcUar6grEw9RP.tyt86vpZ19nL_7Mn
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 02:22 Hello, hi.
Hi, Robert, how was your vacation?
Oh, you already asked here last time.
**Robert Pająk** 02:32 Yeah, hello. Yes, you did.
**Liudmila Molkova** 02:34 I'm sorry, I forgot you already came back and we've already met.
**Robert Pająk** 02:40 Yeah, it's already… yesterday was first day at school, so real life is… is back.
**Liudmila Molkova** 02:48 Yeah, we… it's, it's funny, in the US, we have…
the first Monday of the month is… Labor Day.
**Robert Pająk** 03:02 I know ya.
**Liudmila Molkova** 03:03 So we had the holiday yesterday, so there was no school on September 1st.
**Robert Pająk** 03:11 So it's their worth it later.
**Liudmila Molkova** 03:14 It's fun. We don't have a dedicated date, per country. It's actually different states have different dates. I think California starts in August. We here, we start out my kids. One of them starts school tomorrow.
And the youngest one starts school on the next week.
**Robert Pająk** 03:34 Okay.
Still a few days.
bookcase? Yeah.
**Liudmila Molkova** 03:42 I'm not sure if Trask is coming, let me ping him.
**Robert Pająk** 03:46 I think he might be the Vagin I saw his peer in Java on extended attributes, so he might be just, you know, very occupied.
Maybe I'll pink him?
**Trask Stalnaker** 04:06 So sorry.
**Robert Pająk** 04:08 Oh, you're here, I was just writing.
By the way, do you have a new haircut with the mua?
**Trask Stalnaker** 04:21 I hope they.
**Liudmila Molkova** 04:21 for us.
**Robert Pająk** 04:21 me.
**Liudmila Molkova** 04:25 you a beer cut!
It's, it's maybe a month sold.
**Robert Pająk** 04:32 Okay.
**Liudmila Molkova** 04:32 Yeah.
**Robert Pająk** 04:33 Okay.
**Liudmila Molkova** 04:36 I have a new cat.
**Robert Pająk** 04:39 Oh, but there's a second one, also, upper, but probably it was there already.
**Trask Stalnaker** 04:46 So you added a second, did you add a second?
Cat perch, or did you already have two there?
**Liudmila Molkova** 04:53 So I had one cat, he's 13, he's been with us in 3 different countries, and like, 6 months ago, we've got two new cats. You can see both of them here. They are…
**Robert Pająk** 05:06 Okay.
**Liudmila Molkova** 05:06 Not kittens anymore, but relatively new.
Hmm.
**Trask Stalnaker** 05:33 Alright.
I did push, just this morning, my… the work I had been doing on the complex attributes prototype.
I was still… working on it. But from the perspective of,
I'm not sure that we will… the direction I'm thinking of going is…
Not trying to reuse the existing value, classes, and…
There doesn't seem to be much benefit and kind of only downsides to reusing those, partly because of… but it could be because of how we've built them and structured them already.
Yeah.
So I think the attributes will…
have, and I have modeled it as… attributes are… the attributes class is the map class.
And so it can have… Attributes, classes, instances embedded in it as nested at.
maps.
Yeah.
I think that was kind of the… What we're trying to get.
**Robert Pająk** 07:18 Was there trust anything in my draft PR for the spec that will be against your proposal? Because I personally do not think so, but I just want to double-check.
**Trask Stalnaker** 07:31 I… didn't…
Luck… Follow us…
**Robert Pająk** 07:41 The last line.
**Trask Stalnaker** 07:43 Oh, yeah.
I think we were… if I recall, the discussion we were having the last time…
Was… oh, it didn't add…
**Liudmila Molkova** 08:06 I think we talked for a bit about different names we would… Give it… And I'm decided to…
**Trask Stalnaker** 08:19 Yeah, and then the connection to log, body…
I hate to… the Java… I hate to lean too much into the Java…
Piece, just because we have some… legacy there that… is potentially impacting my… suggestions over there.
**Robert Pająk** 08:54 But it's maybe true also for other languages trust, so, you know… You're so distance.
**Trask Stalnaker** 09:05 I don't know if any… have any strongly typed languages… Implement, stabilized logs.
**Liudmila Molkova** 09:19 Ra… Rust?
**Robert Pająk** 09:23 I don't think they're stable yet.
**Trask Stalnaker** 09:26 log body…
**Liudmila Molkova** 09:42 I think both C++ and Rust stable.
**Robert Pająk** 09:46 C++ only. Rust, are you not sure, like, in the IO state is better.
So I'm not sure. Maybe it's outdated.
**Liudmila Molkova** 09:56 Logs APIs, table, logs SDKs, table.
In rust.
**Robert Pająk** 10:06 So, patterns are always outdated.
**Liudmila Molkova** 10:22 Body any value, it seems rust stabilized any value.
**Robert Pająk** 10:28 And I think they created the type for each signal.
Other results were common.
I'll treat you.
**Trask Stalnaker** 10:41 For the, I think…
This is for log body, any value…
**Robert Pająk** 10:51 Yeah, so they have a different type.
**Trask Stalnaker** 10:53 Oh, but.
**Liudmila Molkova** 10:54 Offer attributes.
**Trask Stalnaker** 10:56 also.
**Liudmila Molkova** 11:01 Yeah, it's also the attribute.
**Robert Pająk** 11:04 If this is what is currently in the spec, In data… logs data model.
**Liudmila Molkova** 11:10 Right.
**Trask Stalnaker** 11:41 I mean, this… Seems like… This does seem like a very reasonable interpretation, I mean, and maybe the most…
Simple, like, from… spec… perspectives…
**Robert Pająk** 12:04 C++ does not seem to implement complex attributes.
Similarly to Java.
**Trask Stalnaker** 12:20 Do they have, log body any value?
**Robert Pająk** 12:25 Trying to find.
Attribute value is gold.
explicitly, it's called attribute value, I can.
**Liudmila Molkova** 12:34 Oh, interesting.
**Robert Pająk** 12:36 Hmm.
I'm just blink it in the chat.
**Trask Stalnaker** 12:54 Okay, so they have… okay, so they call it attribute value and the body also. Okay, cool.
**Robert Pająk** 13:01 Yep.
**Liudmila Molkova** 13:04 Which is what I think we decided last time, or at least discussed, the direction.
**Robert Pająk** 13:23 And there's no complex, because attribute value is from common, so there is currently no complex attribute value.
**Trask Stalnaker** 13:33 Oh, thank you.
**Robert Pająk** 13:35 So probably they wanted to model it in the same way as Wing Go, that they probably, I'm just guessing, that probably they're supposed to have complex attributes, maybe they also wanted to add it everywhere, or maybe it just was, you know.
Maybe it just happens.
**Trask Stalnaker** 13:52 Okay, so set bot… so body doesn't… currently support…
**Robert Pająk** 13:58 You can tweak and probably find the definition, but it doesn't seem so.
**Trask Stalnaker** 14:02 Okay.
**Robert Pająk** 14:05 I can find it quickly.
**Trask Stalnaker** 14:17 Okay, but they're kind of set up to support… Via the attribute value.
**Robert Pająk** 14:24 Yep.
**Trask Stalnaker** 14:48 And just saying this was sort of what we were…
thinking of calling. Is this what you ended… is this kind of what you reverted back to, was the attribute value?
**Robert Pająk** 15:02 Yes, I think this is the exact… I think it should be the exact name in the header.
Currently.
this attribute, I think, yeah.
In this second… In common reason.
Yeah.
**Liudmila Molkova** 15:23 Oh, and I think part of the discussion was that Ugh, we wanted…
languages to have a freedom to call it something else, but the goal might consider
different alias for this type, if I remember correctly, so we didn't want to be super prescriptive on this.
**Robert Pająk** 15:47 And I don't think we are.
You do not force anyone to name it here.
**Trask Stalnaker** 16:05 to read… We're onions here… Yeah.
I like that.
And then for log body… Are we thinking…
**Robert Pająk** 16:22 You're referring to this, yeah.
Exactly.
**Trask Stalnaker** 16:24 Okay.
Makes sense to me.
I like the idea, I mean, given what we've seen, Java's gonna be probably different.
But, yeah, sort of the least… Or the most general name.
is nice.
the body… Being an attribute value.
Little weird, but…
I think it's… I think it's okay, especially that we're kind of… I mean, we're downplaying… body…
At least in the… Events…
**Liudmila Molkova** 18:17 If it raises any concerns, we could return this any and just explain that the any type is the same as the attribute value.
**Trask Stalnaker** 18:32 Right.
**Liudmila Molkova** 18:35 And if you want to alias it or name it differently, go for it.
But…
It also would not be a problem. Well, it would be a,
A backward compatible change to say that the body supports attribute value now, and in future it will support something else called body value, if this need would ever come.
**Robert Pająk** 19:17 Could you repeat or replace? Does I'm not sure if I got it?
it will be a breaking change, right? It will change the…
**Liudmila Molkova** 19:24 Not a breaking change, so if we would ever want to expand, like, if for some reason we would really prioritize event bodies at some point, the log bodies.
And they would cover something else, not covered by the any value.
Then we could, in theory, make this change in non-breaking manner.
So, essentially, I'm saying that
This section can be rewritten in the future if our opinion about event body changes.
**Robert Pająk** 19:57 I disagree. I think if we say that it's a type, then it's basically this type. If we want to have a different type, we should explicitly call that it's a separate type.
**Liudmila Molkova** 20:08 Any value implies any type, right?
**Robert Pająk** 20:14 I mean, if we have any type, then we will need to define it anyway.
You suggest that, because I'm not sure you… you're thinking that we may have a different definition in future of attribute value than body value?
**Liudmila Molkova** 20:38 I'm saying that this door should be open.
We don't want to close the door. I don't want to open it now. I don't see a reason to, but…
I don't want to close it.
**Robert Pająk** 20:53 So one of the reasons why we wanted to have attribute value
It's also the semantic conventions, the generation, etc.
So, if those were a different type than the ones that are
like, we… I think… we think it will be simpler.
If it could be the same types as you have in semantic conventions, instead of, you know, creating a new generating mechanisms, etc.
Because otherwise, if you want to have it differently, then we'll basically copy-paste the definitions to make sure that we want to have, you know, we want to, for example, add an additional field, only one, and not in the other.
**Liudmila Molkova** 21:51 So, on the product level, right, both of them are any value.
**Robert Pająk** 21:56 As long as we have a type that represents all the richness of any value, it would.
**Liudmila Molkova** 22:01 Forever, work for both.
**Robert Pająk** 22:04 Yes.
**Liudmila Molkova** 22:05 And changing it would mean a huge change. It could still be done.
Right? You either make a more restrictive body type.
Or you would make, some, I don't know, different kind of convenience on top of it in the API?
But it would still need to be compatible.
Any way to stay compatible with the protocol. If something changes on the protocol, it's like the end of the world, we do end whatever.
And it's fine either way.
So I think that the door keeps open to the changes. The old weirdness is the name.
The presence of attribute in the name.
But…
**Trask Stalnaker** 22:57 What if we caught… so, let's go… I wanted to talk through the… If we call it any…
Value…
**Robert Pająk** 23:09 I was there, and I'm fine with it. So, just saying that, you know, here in upper, in the attribute, if you, just not even scroll, the attribute value must be one of the types defined in any, basically any value, and it will read also well.
The second bullet point in the previous section.
So, here, the attribute must be one of the types of different in any value. It reads well, if we rename it.
**Liudmila Molkova** 23:43 But if we put that section, like, the attribute value, call it.
Any value and put it above attribute, and then we can link to it from
From attribute, and from the body.
**Robert Pająk** 23:57 Yeah, this will work as well, all the computers are below.
**Liudmila Molkova** 24:00 Yeah.
**Robert Pająk** 24:01 It can be above… it can be above because it's more generic. That works. So, then we'll also need to probably rename attribute collection to something else.
Yes. So, probably you'll need to have two sections. Like, one will be attribute collections, which are the top level, like span attributes, etc, etc.
And second will be, I don't know, any value map.
Or something like that.
**Liudmila Molkova** 24:33 Yeah, I feel like this, I feel strongly about, that attribute collection is a collection of attributes. You can give it to a metric, right? It's not the same as a list, key-value list, inside the attribute value.
**Robert Pająk** 24:49 Okay, so… I can try it.
I was almost there, but yeah, based on…
I think that your trust could lean towards this direction, after your work.
**Trask Stalnaker** 25:04 I think, I'm leaning towards the any value after seeing that…
Everybody's kind of naming it, like, something different anyways.
So, we don't… I don't… I don't think it helps us necessarily in the spec.
**Robert Pająk** 25:28 Yep.
**Trask Stalnaker** 25:29 tried to… Be too precise there, or…
Or not… that's precise isn't the right word, but to match the implementation.
And… If any value makes things clearer when people are reading this back, And…
I think that's a good thing.
Implementations.
maybe call out, yeah.
implementations can use any value, or they can attribute values good, just values good, Java will have something
different. We may not have a type that specifically is called value.
**Liudmila Molkova** 26:28 What should you do?
**Trask Stalnaker** 26:31 So, for example, in… We would just have,
When you're setting it, we would just have all of the, like, let's see, the attribute builder…
Why am I not finding my attributes builder? I definitely…
Oh, right, right, nothing changed in Attributes Builder because it's a generic…
So let's see, attribute… Key…
So, we would have, when you're doing an attribute key, attributes doesn't require a new
Type… a value type, because it's just, again, it's a map, and we already support
We're already restrictive. The attributes builder already only accepts defined types.
Does that make sense?
this one… I would need to do something different, like maybe have attribute key of… attribute list.
Instead of list of value.
basically hiding value.
so that under the covers… because under the covers, I don't want to wrap everything in a value type.
I want to store things, more efficiently.
Just a list of objects.
Or a map of objects.
with… But not with type-safe… way that, Create them.
**Liudmila Molkova** 28:55 Hmm, okay, and then the… the map?
It's…
**Robert Pająk** 29:02 Couldn't you do two things at the same time?
Meaning, making it efficient and type-safe.
I think we did one goal, basically.
**Trask Stalnaker** 29:17 That's what our attributes class already…
**Liudmila Molkova** 29:20 Yes…
**Trask Stalnaker** 29:22 Is it's both efficient and type-safe?
It just doesn't support nested stuff.
So it's easy… in this PR, it's easy to add nested attributes under attributes and extend that type safety and efficiency there.
**Robert Pająk** 29:43 Okay?
**Trask Stalnaker** 29:44 So, the only thing that's remaining that I need to do, for that is… Deal with lists.
So I need something similar to Attributes, and Attributes Builder.
for creating… that creates efficient and type-safe maps, I need some… a similar Class construction for lists.
So that I can store just a list of objects internally, as a sort of list of wrappers of objects.
**Liudmila Molkova** 30:32 So then… you're… To some extent.
Implementing what Robert has, the attribute collection.
And the map value are the same.
**Trask Stalnaker** 30:53 Yeah, unless we say that this is a top level… concept.
**Liudmila Molkova** 31:04 Would it change how you implement it, though?
**Robert Pająk** 31:07 You can, you know… You can still, you know, have it as,
As a body, so it has to be a top level, kind of, right?
Or not necessarily.
**Liudmila Molkova** 31:20 And this is…
**Trask Stalnaker** 31:22 We don't… I mean, we don't need a name. The thing I'm kind of coming to is, like, that…
We don't necessarily have to have a name for these things in the SDKs themselves.
Like, yes, we need a name for them just from a disk to be able to…
document, spec them, like, it's helpful to have a name for things.
But it's not the… the functionality.
**Liudmila Molkova** 31:57 I mean… like, from… implementation, like, from the consumer standpoint, API consumer.
I want to say that this is my… height.
this value, I, like… Speaking in Java terms, I want to implement value hyperextended.
And pass it over.
I don't want to construct it
from… well, I can construct it from the pieces. I can have something, like, two…
Your attribute or something on it.
It, it's…
**Trask Stalnaker** 32:38 Yeah, can you explain that a little bit more, again?
what you want.
From a consumer perspective.
**Liudmila Molkova** 32:47 So I imagine I have a complex thing, right?
I don't know.
A map? A list of maps.
**Trask Stalnaker** 32:56 List of maps, okay.
**Liudmila Molkova** 33:01 what I need to do to use this API. I need to create this subject first.
then I need to convert it into attributes.
Like, I have a model that describes something. It's kind of natural to represent it as a type itself.
The alternative…
**Trask Stalnaker** 33:22 this.
So, if it's a list of values… And…
You would model it using this attributes list.
thing that I don't have.
**Liudmila Molkova** 33:40 Yeah, I mean, just forget about what it is. It would… it's kind of cool.
If I could say attribute key, and give my type, which… Which is compatible with value.
And say, I want the attribute key of this type.
And then I can have some type safety, because otherwise, Like, I can create… Objects that are attributes, right?
**Trask Stalnaker** 34:16 You want to serial… be able to serialize an arbitrary object.
**Robert Pająk** 34:21 Yep.
**Liudmila Molkova** 34:22 not an arbitrary, not necessarily an arbitrary. It could contain, like, if it… if there is a value.
And it implements a value, or you can convert it into value, than…
You can implement, like, serialization inside this.
Type.
And it doesn't have to be arbitrary object, it's a very special object.
**Robert Pająk** 34:49 I'm not sure if I was saying the same, I will say the same or something different, but here I see only, I think.
an ability to create an attribute with a key, right? A key value.
And for the body, you need to just con… create the value, only the value without the key.
Right?
Or is it just attributes?
**Trask Stalnaker** 35:20 Sorry, I didn't follow your…
**Robert Pająk** 35:23 The attributes will create some
how would you create just an attribute value that contains a map? It's in the attributes… the attributes, factory, or something like that?
Some constructor of attributes.
**Trask Stalnaker** 35:40 How you would create the map?
**Robert Pająk** 35:43 Yes.
**Trask Stalnaker** 35:45 Attributes is the map.
**Robert Pająk** 35:50 How would you just create the, the, the… Okay, the map without, okay…
Got it. What about the array?
**Trask Stalnaker** 36:06 We don't have… that's what I currently…
I think to implement that, I would… I'm currently thinking of introducing a new class.
That hides value, and is, like, attribute list.
**Robert Pająk** 36:25 I see. Something like that. So, attributes and map, I see. For primitives, you're just using the primitives? You do not have a distinct type for it?
**Trask Stalnaker** 36:34 Right.
Right.
**Robert Pająk** 36:36 So you're just free, you do not… I see.
Instead of having a union type, like we do, you just create each type by themselves, like, self-contained.
And you just add functions overloads that accept all of this stuff, which is not possible in Go, because there's no overloading.
We'll need to… yeah.
**Liudmila Molkova** 37:01 So d- this?
This allows, like, if it's implemented, however it's implemented, it allows to create any value.
maybe what I'm asking is the next step, that if I want My convenience around any value.
Let's say I want to have an API
Generate a method that takes attribute key of type.
I don't know. Gen AI, whatever, complex stuff.
And it would be… Who?
it would require exposing value, because we… like, what I want our idea is that you create one object, and then every time you use attributes, you convert it into the attributes, right? It's very expensive.
I want to… to create an object, and it…
And for it to also service the attribute value.
I can probably still do this, I can wrap it in some convenience.
And then I can…
**Trask Stalnaker** 38:11 Would you… so, when you're serializing it, would you serialize it
Each time, like, why not have, like, why doesn't two attributes… on your…
Object work, if that's what you want, is a standard way to convert it to an attributes list.
**Liudmila Molkova** 38:54 Well…
**Trask Stalnaker** 39:05 Because I don't think… it's not like you could implement… value…
anyway, right, you would need to implement something that Serializes it to value.
**Liudmila Molkova** 39:22 Thank you.
**Robert Pająk** 39:22 process.
**Liudmila Molkova** 39:23 huh?
**Robert Pająk** 39:23 Trust, how old processors work?
How would you know when in a log processor or trace processor, what type is of… what is the type?
**Trask Stalnaker** 39:35 That's a good question.
to… what we do today is… I mean, you get the types, right? Like, we just return it as, like, a map
Of, like, you get your key-value pairs, so you'll get…
String is always the key, and your value might be a double, it might be a long, it might be a string, it might be a list.
It might be a nested map.
So I think we would probably extend it in that direction.
**Robert Pająk** 40:16 You can get, what kind of type…
**Liudmila Molkova** 40:18 fish.
**Robert Pająk** 40:19 But you have an anom, right, that says what it is, right?
Inside the attributes.
**Trask Stalnaker** 40:26 We have attribute type. Yeah.
So you can check… Yes, you can check attribute type.
**Robert Pająk** 40:36 Okay.
**Liudmila Molkova** 40:51 Okay, so… I'll… create something… that chose.
Or are they… Think would be useful.
It doesn't mean… it contradicts anything on this PR.
**Robert Pająk** 41:14 I think… I think the… the thing is that in the attribute type right here, I think that the attribute type is only used in the collection, so it is to gather the key value, and this is where the enum is used.
But for the collect… for this… least collection.
You just need to have the attribute type even for this, you know, single value without the key, right? Probably you had it already here.
Or you're just working on it. In this, you know, attributes, list, collect, type, or whatever. Probably you will need to contain, something would be a value, and this endom, right?
**Trask Stalnaker** 42:07 I don't know, let me see what we do for… yeah, that's a good question.
Because for maps, at least, right, we don't have to worry about null s. Is that your concern?
Is that no… if it was null , you don't have a…
You can't determine the type from that.
**Robert Pająk** 42:30 I mean, I think that consumers will prefer to have annums to know what they correspond to, instead of knowing all the possible types and primitives.
Because then the documentation can say, if you have this kind of random, then it means you can test it to this thing, for instance. Or you can have some, I don't know, helper functions.
**Trask Stalnaker** 42:54 Yeah, let's just see what,
Is there today, though, because that ship might have sailed.
Already.
Yeah, I guess you…
**Robert Pająk** 43:08 We have it already for the… I guess you will have it in attributes, probably, even.
**Trask Stalnaker** 43:16 How does this work?
**Robert Pająk** 43:31 That's what I would expect it to be.
**Trask Stalnaker** 43:37 So… Oh, for each, this is what we do.
So you get back… attribute.
key, so for the maps, you do get back attribute key, Oh, yes, because…
the attribute key isn't really a string, it's the attribute key object, which has the enum. Okay.
So, I understand your point about lists, then… Not… Yeah. Okay.
**Robert Pająk** 44:17 They do not have the key, so you'll need to have an interface, or…
Class or something, which is just the object, and the type without the key, without the string.
**Liudmila Molkova** 44:31 Or it can be a list of attributes.
As well, where if the… if the map has attributes, then… The list of attributes.
There's all this stuff maps.
**Trask Stalnaker** 44:43 Yeah, which, I mean, would be okay… I mean, you can… You could, in theory.
**Liudmila Molkova** 44:52 Mmm.
**Trask Stalnaker** 44:53 That… the type of the object in there?
And,
But it's not…
**Liudmila Molkova** 45:05 You would need to check if the subject is an attribute key on its own. Sorry, the attribute.
If it's in attributes.
instance, right? Yeah. Yeah.
**Trask Stalnaker** 45:17 Yeah, yeah, or if it's an instance of long, or double, or…
**Liudmila Molkova** 45:21 Yeah.
**Trask Stalnaker** 45:22 another list.
**Liudmila Molkova** 45:23 Which you would do today anyway. You would need to check the type… well, you check the attribute type.
And you interpret that…
**Robert Pająk** 45:32 Yep.
**Liudmila Molkova** 45:32 Yeah, the object.
**Trask Stalnaker** 45:35 Yeah, you can kind of do… yeah.
You could do either. You could… but yeah, it's nicer. You can, just use the attribute type from here, and do a switch on that.
We don't have type switches in Java.
**Liudmila Molkova** 46:00 Yeah, it… That, it boils down, you could do processing.
**Trask Stalnaker** 46:07 Yeah.
Yeah, I mean, I'll… to… I'll… Play with that, here.
I guess for a… hetero…
Yeah, I'll have to see, like, pros and cons there. I mean, I certainly want something that's going to be efficient.
But maybe lists… Yeah, we'll see. Okay.
Sadly, we can't. In Java, we don't have,
memory-efficient lists, whatever you call them. We can't, they're all gonna be pointers,
I can't pack them into a list.
What?
I assume that's what GoStrech will do.
I think we are creating some arrays, yeah.
But you get a memory-efficient… you get a memory-efficient, list of your pairs.
**Robert Pająk** 47:18 It's very hacky, but that's what we're doing.
**Liudmila Molkova** 47:32 Essentially, Java will not have a value, it will be hidden from users.
**Trask Stalnaker** 47:40 That's what I'm proposing.
Currently.
From an efficiency.
perspective.
**Liudmila Molkova** 47:58 How… Like, it's, it's something I, we talked… Previously.
It looks weird to me that attribute collection is also a type in the nested.
Type nested inside the attribute.
I couldn't come up with any specific case where it's bad, it just feels weird.
**Robert Pająk** 48:25 Yeah, I tried to… I tried to rename, rename it, so if you open the agenda.
Yeah, I…
**Liudmila Molkova** 48:38 It's interesting that you had a TRPR, and a Trask had it in his prototype.
So, if we…
decide that it's bad for the spec, then we should also not do it in Java. If we decide that it's okay in Java, we should not, like, I mean…
We can keep this pack, probably.
**Robert Pająk** 49:04 So maybe… maybe I will not do anything yet.
**Liudmila Molkova** 49:09 I just…
**Robert Pająk** 49:09 wait for Trask feedback.
**Trask Stalnaker** 49:16 I'm not going to,
Keep in mind, this is just my proposal. I don't think we're going to get any…
We really need Jack… To nail down what… We will do.
end up doing in Java.
I mean, sometimes…
**Liudmila Molkova** 49:41 Well, did you feel it's okay? Like, I mean, I'm curious, like, what were your thoughts?
**Trask Stalnaker** 49:48 My thoughts… my thought is that we…
need something. I… I don't really want…
To compromise much on the efficiency aspect.
And… Then there's the other piece of, I also don't want to completely rewrite.
everything, so I want it to fit into… our existing… attributes… Class?
So… that, I mean, I could certainly… From a separating… Top-level things out.
I could… I think I could…
Create a… Essentially, a copy of the attributes, class.
That is just meant for… nesting.
**Liudmila Molkova** 51:17 Yeah, I mean…
I'm… I'm testing my taste, right? It's my taste that it feels weird. It seems like it didn't feel…
**Trask Stalnaker** 51:26 I agree. No, no, no, I think it does feel weird.
I agree there's a degree of weirdness there. It's one of a few things that are weird.
Similar to the body… I think the body value thing is more weird to me.
I think I can kind of live with the attributes being
Also from the perspective of… Flattening things… Just nesting things.
But I really… I don't mind… I can definitely try that, like, this could be…
And maybe it… maybe I'll like it even when I have to name something new for this one, for the list, like, attribute list, I could call this attribute map.
And…
That would be for… Nesting, specifically, and attributes could stay the top-level thing.
That could be nice.
Yeah, the… I… I'm definitely in for exploring not being weird.
the two constraints, I think, from the Java perspective, are…
Efficiency, which is why I'm shining away from exposing that value.
Object, although maybe there's other creative ways to do that.
And then the… Or, like, fitting into the existing structure.
**Liudmila Molkova** 53:32 Right.
**Trask Stalnaker** 53:33 But… this… Would fit into the existing structure.
I don't mind copy-pasting code, or inheriting, or composing, or anything like that, it's…
From a rewrite, I just don't… I don't want to deprecate…
Right, yeah. A bunch of stuff.
So, to the attribute value…
I mean, I do like the idea of the spec being… Sort of our ideal, like.
As clear as possible.
Given that… We're going to have different… People are gonna name things… Differently… Have named things differently already.
But we can come back to that next week after, with my latest prototype.
Also not sure when Jack… Is gonna be back.
So I may ping him just, once…
Maybe once we get a little bit further along with that prototype.
**Liudmila Molkova** 55:17 Cool.
It might be that…
**Robert Pająk** 55:26 double-checking, because my family returned, and I had a lot of background noises. Is my bullet point up to date, or not really?
Because I heard, like, 50%, and I tried to guess so.
**Trask Stalnaker** 55:39 No, I think… I think in Java, what I'm going to, try is…
this change. So, A, I want to see what it looks like To hide value completely.
I'll have to see what that looks like on the consumer side. I mean…
The processor side, to your point.
And then,
Oh, yeah, but I can probably do… okay, yes, I think I can act that in a hacky way.
And then see what this looks like.
So I think that's… that's some good feedback on the… the… Prototype.
I can make more progress there.
**Liudmila Molkova** 56:46 Thanks a lot.
**Robert Pająk** 56:50 We are… almost a… At the time.
Do you think that I can just open the PR for public?
Just interrupting it, despite PR.
**Trask Stalnaker** 57:06 My only thought is it would be nice, like, as kind of a big change to the PR, whether you restructure it with any value at the top there.
**Robert Pająk** 57:19 Okay, slow, okay, let's wait.
Or more feedback then. For your feedback, right?
Or you want to do it, because I'm not sure, because what I see for your proposed change, like this attribute list.
and attribute map, you still have this attribute naming. We have the same for Go. We say… we saw the same in C++.
So… I'm just not sure if it's…
From the one side, I would like to have a different name for this concept. On the other side, I'm not sure if it's not just overcomplicating and not creating unnecessary terminology into specification.
And if it couldn't be also restructured later.
**Trask Stalnaker** 58:08 I think spec readers are gonna find the any value Type, clear.
**Robert Pająk** 58:15 Easier to read.
**Trask Stalnaker** 58:16 Because they're familiar with any value coming from.
**Robert Pająk** 58:20 Okay.
**Trask Stalnaker** 58:21 And it's a name for the thing, and it doesn't conflict with body, like, the body… the… we're gonna get, I think, less pushback on that.
I think overall, there's less… That's less controversial.
I was interested in the more controversial approach of trying to come up with a name
for the thing that we would use, standardize, use across SDKs.
But it kind of feels like that ship has sailed with…
We've already got a variety of names.
**Liudmila Molkova** 59:06 the ship has sailed on C++ and Rust, but if we…
If we are prescriptive, there is a chance that other languages would follow.
And would have at least some consistency.
**Trask Stalnaker** 59:21 Yeah, I'm not seeing that Java's gonna follow, though.
If we don't.
**Liudmila Molkova** 59:26 Oh, you're doing it wrong, yeah.
**Trask Stalnaker** 59:28 Yeah.
**Liudmila Molkova** 59:30 You're not exposing the type, which is also the consistent choice. The .NET might follow this choice.
I have to go.
**Trask Stalnaker** 59:44 Thanks a lot.
Nope.
**Robert Pająk** 59:47 y'all, things.
**Liudmila Molkova** 59:47 year-round.
**Robert Pająk** 59:48 Bye.
