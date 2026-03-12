SIG: Arrow SIG
Date: 2025-09-04
Duration: 50 minutes
============================================================

## Zoom Recording Transcript

**albertlockett** 00:46 Hey, Laurel.
**Laurent Quérel** 00:48 You will do.
**albertlockett** 00:49 Hello?
**Laurent Quérel** 00:53 What? No, that's all.
**albertlockett** 00:56 avec… Oh my god, this un peu complicer de… je pense que j'ai une solution, mais… a chisie.
**Laurent Quérel** 01:16 There go. Okay. Bye.
c'etait… receiver qui, qui vous et pas le jebe.
**albertlockett** 01:37 Cool. Hey, Josh.
So I'll switch to English.
**jmacdonald** 01:42 Y'all are speaking French, I think.
**albertlockett** 01:45 Yes.
**jmacdonald** 01:51 Microphone, okay.
I may have to disappear at some point during this hour, for a contractor that needs to talk to me.
That may happen.
**Laurent Quérel** 02:05 for Clinton.
A ton of, tons of things happened during the last one, two weeks.
I have a small demo to do, if you want.
See, I will add my.
**jmacdonald** 02:38 Yeah, so maybe since I could have to disappear, I would briefly speak, about the work I've been doing.
I will be back by 9 o'clock, and I will be able to review the PR. I started looking at the yours, Laurent, And, The endpoints.
We'll approve that.
I think I'm ready to approve it right now. I don't… I read it.
I'm gonna make sure Albert approves.
**albertlockett** 03:11 Oh, yeah. It looked good to me, If it's the one I reviewed yesterday or the day before.
**jmacdonald** 03:23 So, I think we should just go, because I'm not… I wasn't expecting any visitors for this meeting. Maybe we will, but we'll see. and since I might have to disappear. So, Yeah, I'll share for a sec. Here we go.
**Laurent Quérel** 03:45 Yeah, okay, so I've been working on,
**jmacdonald** 03:49 Modifying the retry processor to use a back propagation mechanism.
That meets… the design criteria, largely following a design that Laurent sketched out for me, so I'm… I've been implementing this and learning as I go how the pipeline engine works.
This is my second iteration. Laurent gave me some feedback on Tuesday, which I've now applied.
The, The pieces I want to show you are… I suppose I should scroll through in a natural order. So, I want to get to the… let's get right to the bottom of it. So I've extended the PData interface in the OTAP package. At some point here, I decided that this PR was too big, it's not a single PR anymore, and I wanted to, like, learn some things and… and do some things. So there's a couple extraneous bits here I want to show.
So… so to start off, here's the big, big change, is I've modified the OTAP P data Type to be a struct.
consisting of context, and the former thing, which was now… is now called OTAP Payload. So OTAP Payload is the… Is… Oh, it's below. Things are not in the order I expect. So, I'm gonna scroll down a little bit to show you that… convince you that OTAP payload is the same thing it used to be.
God damn, I can't read anything. Okay, so here it was. It was an enum.
And it has now become… the same thing.
Except it's not in order that's making sense to me right now, so I'm not going to show it to you. Let me show you what matters. So I have… extended that OTAP payload with some interfaces that allow me to take the context, or to take the request payload out of it, and I'll show you how I use that. I've also added, a test called isEmpty. If you take the request payload out, it is now empty. That's the logic that we're looking at. This was maybe extraneous. I have a point in my retry processor where I say, okay, I sent you the data, it came back.
And I expect to have payload here. If it's empty and it came back with empty, it's like internal error. I was expecting my payload to come back so I could send it again, and I didn't get it. That's why I'm going to use isEmpty.
someone accidentally takes the payload, it would be an internal error. So here's take payload. I added num items. This is just, like, a thing I feel that I want from working in the Go Collector. Like, most payloads in OTLP have a defined number of items. This is a standard.
I… but I made it config test, and the reason why is that I made it consume itself. Why? Because I'm… I'm torn about how to do some things, and this is what I wanted to talk about a little bit. So, I have num items consuming self. Why? Because the OTAP arrow bytes form needs to modify itself before it can count itself.
That's the… that's the upshot. This was my extraneous thing. I had already written a test helper in one location that did this for the OTLP bytes. I wanted to see what it would look like if I generalized it. Now I know, and I'm not sure what to say about it.
So…
**Laurent Quérel** 07:10 But, so the OTLP bytes also needs to be, transformed.
**jmacdonald** 07:14 No, we can use the view mechanism that we have to count items in an OTLP bytes without modifying it, but the OTAP bytes.
**Laurent Quérel** 07:22 Hmm.
**jmacdonald** 07:22 protobuf struct, and we don't have a way to count them yet. That could be a fix.
This was me, it's sort of a dead end, my num items thing. So ignore num items. I told you about isEmpty. I've made a new function here called CloneEmpty. Laurent, you mentioned the idea of having an empty state. Like, we have an enum called OTAP payload, which is logs… which is, sorry, it's OTLP bytes, OTAP bytes, or OTAP records.
And if I'm going to be able to take out, I need a default implementation, but when we have these enums, the only way to make a default is to add a new branch of the enum.
which would be something like empty state. And I thought about doing that, and then I went a different direction. And this was a sort of experiment, so we'll see what it looks like to you. The reason was that I… I didn't want to invent a new state. Instead, what I tried to do…
**Laurent Quérel** 08:10 you, too.
**jmacdonald** 08:11 was to preserve the structure that I had, which means to keep the signal type.
Because the signal type is buried beneath two enums, and if I just have an empty state, it means having to handle an empty state in a bunch of places where I'm, like, not going to know what to do. Here, instead, I just have an empty type of the same original structure. And that… so… so I'll show you what that looks like. Now, so there's this helper type. I renamed it, didn't make sense to me to call it helpers, but whatever. So then this is the pattern that we already had. Signal type was already here, clone empty just… Returns the appropriate type. This is for the OTAP arrow records.
So, OTAP Arrow Records implements default.
So does… So you can… you can take it, and you can… Clone it empty with default.
Is empty.
This was, like, again, I don't think I should be counting rows to test if something's empty.
But, I don't know. This is, again, me kind of learning what I'm doing.
for the OTAP arrow records, counting… counting num rows looks like this. I think that's the correct code. Okay, so now… For the OTLP proto-bytes. Clone empty.
Puts a new vac in.
is empty, checks if the vector's empty. Take payload, does mem take, because it works. Num items.
uses the iterator.
The view iterates over the view.
And we don't have metrics yet for that.
Now for the OTAP arrow bytes, this is where clone empty can use default, isEmpty can use isEmpty.
take… on the payloads, that's… that's, like, a little bit editorial here. A take payload can do mem take… But num items, this is where we call try into, that's why I consumed the object. Again, extraneous side quest for me, learning what I'm doing.
If I may continue a little bit further, so now all these conversion functions use the payload.
There's not much else to see in this file.
Now I want to show you the kind of meat of the retry processor.
As I've done it. So, with a… with… with, I'm just… just to say, David, like, you… you put a good start together here. I've erased all… I've commented out all the tests and… and deleted all the state, but… but the framework is still in place. So, So, I removed a couple fields from the retry config, there's no more max pending messages, there's no more cleanup interval, because it's… it's not got any state of its own anymore. So, let me get to the bulk of it.
so I've created this new type called retry state, and… At this point, I don't believe I even need the second field, I just need to count how many retries I've done.
There are some open questions here about context and deadline, and… but… For the moment.
Ignore that detail.
what I want to show is… I… so I have… This is a naming question I haven't resolved yet. I have a reply state and a retry state. Reply is a generalized thing in the engine. When you get back the NAC, you can see the reply state. It's just two registers, so… so into or from on the retry state lets me produce the reply… the retry state, which is the typed fields.
So those are converted from a general representation in the PDW context back into my specific implementation. There's a vector of those reply states in the context. It's like a stack discipline, so… The part I want to show you is down below a little bit. So here we are, handling… a P data inside of the retry processor. First thing I do.
I say, do I have a reply? Like, is anyone waiting for me to reply? Because if there's not, if someone has sent her a thing with no reply information, then there's just nothing to do.
So if there is a return node ID… I mean, if there wasn't a return node ID, I don't know who sent me this, but it came in my channel.
I call data.context, that's a mutator, I call replyTo, I give it my… my identity to reply to, that's my address in the pipeline controller, and then I copy my Rstate, my reply state, into. So this becomes pushed onto the stack of the context, and then it gets sent Right here.
So, we push our thing onto the context reply to stack, and we send it.
So then, on the return path, we get back an ACK, it doesn't do a whole lot. It pops off its own reply state. It's not going to use it anymore, because it's had success, so it's dead information. We popped from the stack.
We then, figure out who the next responder is. I already checked that this exists. Assuming stack discipline, this will be the same value that I checked up above.
And then I… I send the NAC.
Assuming I have a return to address. That's a simple case. I wrote a comment here saying, I expect almost everyone who receives an ACK is going to do roughly the same thing as I just did. So you could imagine rolling this feature into the pipeline controller just to say that I didn't subscribe to the AC, just, like, pass it backwards. I only want an AC, maybe.
In this case.
So then the knock case, I, first thing I do is pop… my reply state, turn it into my retry state. Now I can.
**Laurent Quérel** 14:06 Wait a minute.
**jmacdonald** 14:08 Please.
**Laurent Quérel** 14:08 Knowing how work… so the… the entire system is relying on the speed data message, where people… Where nubs can specify their interests.
And then, there are interests for ARC, or for NAC, or for whatever we can imagine in the future.
How is it possible, to receive something that you didn't ask?
**jmacdonald** 14:45 I would modify this reply to call to say, I'm interested in the NAX, not the X, maybe?
**Laurent Quérel** 14:53 No, no, I mean… you already mentioned that you are interested by the ACC or the NAC, because you specify when the… when the… the first time that you… you received a PDATA on the PDATA channel, you specified your interest inside the PData. Then you have a reply.
let's say the retry processor received now on the control receiver, not the…
**jmacdonald** 15:19 Yep, that's… that's what we got right here.
**Laurent Quérel** 15:22 Yeah, and receive a hack or NAC, but if this node receives one of these events, control message.
It should be by construction, because you already specify your interest into the initial P data message, right?
**jmacdonald** 15:37 Yeah, I'm trying to sub… I'm trying to illustrate how there's a condition here, like, I only really want to do anything for NACS. My… my… well, all I'm doing for the ACT case here is propagating it. There's nothing happening here, except… taking the message and pushing it back into the node control, right back to the pipeline controller, saying, I don't care, just send it to the next guy, because it's a success case.
**Laurent Quérel** 15:59 But in the first place, you don't have to put your interests, so you will never receive this message, right?
**jmacdonald** 16:05 But you're interested in NACs, so it's… I don't know at the time I send this reply to whether I'm going to get a NAC or a NAC, and I'm suggesting that the reply… the retry processor only handles NACs, it doesn't handle ACX.
**Laurent Quérel** 16:17 Yeah, but you didn't basically populate the hack interest list.
**jmacdonald** 16:23 Yes, so…
**Laurent Quérel** 16:24 So you will never… you will never receive back message, that's why.
**jmacdonald** 16:27 interest, no AC interest type of signal, I think.
**Laurent Quérel** 16:34 Yeah, so if you have no hack interest, it's determined, when you receive, for the first time the PDATA message.
In conclusion, you will never receive an AC control message.
from anyone, because you never specify that you are interested by that. So we already have a subscription mechanism.
**jmacdonald** 16:53 That's what I was getting at. There's no subscription mechanism here. What you said makes sense. So.
**Laurent Quérel** 16:59 Hmm.
**jmacdonald** 16:59 what I would do is I would indicate the subscription type, like, I only want the NAC here, and if… if I… if I… if you're gonna send me a NAC, forget it, just get… send it to the next guy, is basically what we're saying.
That makes sense. I will… I will carry on. That's what the to-do here was telling me. So, yes. Now, the NAC case, so I popped from the stack, I put it in my retry state struct.
This is a… This is an error case now. We checked before we sent the reply… set up the reply state that we would have something on the stack when we came back, so that would be an error.
Now I'm actually doing business logic of a retry processor. So first, if it's NAC permanent, I prepend the message, but it's still a permanent message. If it's too many retries, I prepend the message too many retries.
I don't like the way it's too structured. Anyway, or if the request was empty, that was that internal error case, I'm like, I don't know how to send this anymore, because there's no data, then I put an internal error. Otherwise, false.
And then the condition has failed. So if I've failed by any of those three ways, I will send a NAC. And I've modified the NAC a little bit, but not much.
Then, this is more or less copying David's original logic. I increment my retry state, because we're going to use POW, math POW.
I have some comments to myself, but then, I compute now, I compute the delay, this is all the original code, basically. I compute the next retry time.
Now, I haven't actually set context deadline anywhere, but it's an optional instance, so it's not set anywhere, but I'm checking if I will expire before my next retry, and the Go collector has the same exact logic, then, And honestly, dealing with time and rust is new and confusing to me.
duration since is the weirdest method name I've ever seen for a chat test before or after, but as far as I understand, this expression, deadline duration since next retry, will be zero if the deadline has passed.
And it will be non-zero if the deadline is not passed. So if it's zero, then I've expired. If I've expired, I'm going to send a NAC.
I probably want to change the NAC message here as well, like… To, you know, deadline expires before next retry.
Then, we're back to… we're back to retry, finally. The to-dos above aren't done yet. Hang on just a second. So here, here I just… I'm calling the same exact reply to method, which pushes onto the stack my… my current rstate. So I've modified the Rstate, I push it back on the stack to call the guy, the pipeline again.
The only to-do here… is that I need to delay until the next retry time, which means sending a pipeline timer message and waiting, or something like that.
The challenge I ran into there is that I think the timer message should have an optional P data in it, so that I can put my P data into the timer queue.
wait for it to fire, and then still have my P data.
That's… that's what I was imagining. I wanted to run it by you all.
Otherwise, I have to put some state here in the retry processor, which, Laurent, I think you were encouraging me to try and avoid.
**Laurent Quérel** 20:31 Yeah, I think the whole point of this approach was… Avoid states.
**jmacdonald** 20:38 Yeah.
**Laurent Quérel** 20:39 as much as possible. I need to think about it.
Yeah, there is a lot to…
**jmacdonald** 20:46 There's a lot here, I haven't shown you everything.
**Laurent Quérel** 20:48 the JS, and I think that, yeah, we… I definitively need to provide feedback.
**jmacdonald** 20:55 So let me just quickly give you a tour, then. I think I should probably stop presenting, but… so the register is, like, an enum of uSize, instant or none. The reply state is two registers. The reply to on that stack is an address and a register, a set of registers. It's useize node ID and reply state.
Context is here. This is… I call this a placeholder. You are going to think about this, Laurent. I don't have any strong feelings right now.
This vector is the main struct that we're passing in the P data that contains the reply stack. If we start putting more fields, it's just going to mean more copying. Maybe the deadline belongs in the reply to stack. I have thought about whether components ever shorten deadlines before they send onward. Probably happens. I just don't have any thoughts more than, like, somewhere we want a deadline.
To get this, to get this to build, sort of, like.
Kind of easily. I've added a new default.
**Laurent Quérel** 21:53 The context here with the stack and reply to.
I'm sorry? Yeah, so I, I think it's, it's, There are things missing now.
It's a stack of what? A reply for what?
**jmacdonald** 22:18 interest in receiving X and Nax at the moment?
**Laurent Quérel** 22:22 Yeah, but, I think what we want is, the ability to create Interest… stuck.
propagate any type of signal, so today it's… it's NAC, tomorrow it's AC, and after it's maybe also something else. But what I'm saying is… And, sir, first, why you have only one stack?
**jmacdonald** 22:47 I expected this was coming, like, I think that we might want a context… a deadline stack.
Reply to stack.
**Laurent Quérel** 22:57 Yeah, okay, okay, that makes more sense.
**jmacdonald** 22:59 some sort of stack for any… and that's actually how GoContacts is organized as well. It's like, you push a new value, and you can look them up, but you're just gonna find the last value of a particular key.
**Laurent Quérel** 23:09 Hmm.
**jmacdonald** 23:09 And then when you finish using a context, you've naturally popped it.
**Laurent Quérel** 23:13 Yeah, so those stacks are, in fact, the interest list that we use to, per signal type.
Organize as a stack in order to backpropagate the signal, accordingly to the interest defined by the nodes.
**jmacdonald** 23:34 Yeah.
So… I… I could imagine a hash map of vectors, where each… each… there's a key and then a stack per key, maybe. And I can imagine… Some optimization approaches to make it, like.
Each… each position on this thing knows which Which vectors it's pushed onto, and something along those lines.
So placeholder for a context type that we like, I guess, is really what this is, and I don't have any strong feelings.
I'm definitely feeling stronger at Rusco.
**Laurent Quérel** 24:14 Luce.
**albertlockett** 24:15 That's good.
**Laurent Quérel** 24:16 Yep.
This is what I had. I feel like I'm looking for help.
**jmacdonald** 24:22 What I will do next, if I don't have feedback or guidance or steering from you all is, to go extend in the minimum way possible the timer mechanism in the pipeline controller to let me put the PDA in there and get it back. That will be sort of, like, my minimum viable…
**Laurent Quérel** 24:41 For the… the expenditure back-off?
**jmacdonald** 24:45 Right, to wait… to put in that delay. And then we can keep thinking about the context and the staff questions that we have.
**Laurent Quérel** 24:53 Okay.
Okay.
**jmacdonald** 24:57 Maybe take the deadline out entirely for now, since we don't really know how I haven't focused on that aspect. I put a lot of effort into the exporters. I don't know if I should show you guys. Does it feel, like, worth talking about?
the point where I take from the… Let me show you.
Again.
So, here we are in the… I don't know which one we're in. OTAP Exporter.
So we get a P data, and I've called it MUT message.
First thing I do is take the payload.
The reason is that we're gonna potentially modify the payload format. So… so I take the payload out, I try into the payload type I want.
Now, this save reply is the thing of, like, if there's a subscription, what I'm going to do… is, take the context out of the message, put together a copy of the data to send backwards. So then what I do here is I pass in the modified payload that has the correct type for this retry.
And if it fails, I will end up sending this… this P data back.
So this PDD is the original context, and a copy Cloned copy of the modified data.
**Laurent Quérel** 26:28 Can I ask a question?
**jmacdonald** 26:30 Yes, please.
**Laurent Quérel** 26:33 Let's imagine an OTLP receiver a very basic pipeline, OTLP receiver, retry processor, OTLP exporter.
Right now, when we don't have the retry processor, the message is not deserialized, is not serialized.
So we are in a very, happy pass in terms of, processing.
Why, fundamentally, the retry processor will, change this, this, this, this optimization?
**jmacdonald** 27:10 The retry processor doesn't. This is the exporter, maybe.
**Laurent Quérel** 27:13 Oh, sorry, my brother, I was.
**jmacdonald** 27:16 Sorry. This is the exporter path. I was… I was going to say, like, this PR consists of touching the receivers, the exporters, and the processor.
John.
**Laurent Quérel** 27:25 I was late. Okay.
**jmacdonald** 27:28 Where I know what I'm doing. And on the receiver, I've done nothing. I've just done new default with no deadline. The next step there would be to parse the gRPC timeout, put it in the thing… And… Deadline is… is, like, really not well… I would say not… a lot rigorously implemented in the Go Collector, but I think the gRPC framework makes it pretty reasonable to think about doing so.
I have never… seen a processor that would say something like, okay, I need one second after this request returns to do some more work, so I'm gonna subtract a second from the deadline and send it on.
And wait for it to come back, and then hope for one second left.
doesn't… it doesn't work very well, like, the… that sort of thing, Dealing with pipelines and deadlines is not necessarily straightforward. So I put it there as a, like, thinking that this is normal.
gRPC expects me to do it.
But when you have a sequence of processors.
And, deadlines, like, it's not always clear what you should do.
I would leave it there.
**Laurent Quérel** 28:41 14.
I'm good.
Yeah, my, so regarding those three lines,
**jmacdonald** 28:48 I'll show you a receiver.
**Laurent Quérel** 28:50 Probably we could imagine that we have, I mean, we don't… I mean, I don't think we need to show all the detail, Probably exporter, auto… We should have, in the incoming message, a method, giving you a way to save the reply.
I'm not sure that we need to.
**jmacdonald** 29:12 Yeah, I did nothing with the root. Okay.
I will keep working on this.
**Laurent Quérel** 29:18 Thank you.
**jmacdonald** 29:22 I'm gonna go see if they need me right now.
**Laurent Quérel** 29:38 So, Albert, you want to talk about the IPC stream?
**albertlockett** 29:42 Yeah, sure. So, the issue that Chris would… Chris had identified… Was that, we receive our… OTAP data in these, messages called batch error record, and inside that is the, the IPC serialized data.
And then we just send that batch error record along the pipeline, and lazily deserialize it if we have to. So the… issue, I guess, that we're running into is that, if you just receive a message midstream, and then say, okay, I'm gonna, you know, IPC deserialize this thing, well, you might have lost the stream state that you needed to deserialize that thing, because in aero IPC, the first message comes The schema, and then comes the record batches, and sometimes the record batches, or the messages might have, you know, dictionary deltas as well.
So, like… when we forward the messages, I think that we also need to send, The consumer, which is the data structure that we have that has those in-process stream readers.
So, like… Does that make sense? Like, we have this, let's… Oh, there's this thing called… the consumer that has these Arrow IPC stream readers, and then every time it receives a new schema ID, it resets the stream reader for that type, basically.
**Laurent Quérel** 31:24 Yeah, sure. But what I'm… what I'm… why I'm… I'm saying, hmm… It's because… For me, the state for a stream should stay on the receiver side, or on the exporter side. I don't see why this state needs to be Why does the set need to be, communicated with the, let's say, what is inside the pitata message when it's an arrow?
Recall.
**albertlockett** 32:02 Because we… because we deserialize the message lazily.
So, like… like… Yeah, so it's like, you might, like, for example, like, the issue we're running into is you receive the P data at the OTLP receiver, and then when the perf exporter tries to deserialize it, it gets this error that's like, hey, you're trying to deserialize some IPC stream bytes that I don't have the schema for.
Okay, good.
**Laurent Quérel** 32:33 Interesting. So the, So, what are the… I see an option, but what are your options?
**albertlockett** 32:43 So, my option would be to put, like, in the… in the PData representation of O… of OTAP.
bytes?
an ARCMUTEX consumer, and that's the consumer for that stream that has the set of.
**Laurent Quérel** 33:04 You know.
**albertlockett** 33:04 computers for those schemas. And then, when we have to convert between, The byte representation and the… whatever other representation, the arrow record representation. We already have the consumer that has the stream state that it needs.
do that conversion.
**Laurent Quérel** 33:26 Yeah, so… I think it, I don't think it's a good idea.
Because if we, if we put things in perspective, So, we, we, we decide… so, right now, we have three states for this fee setup, and, we can avoid solidation, desalidation of a TAP, which is, we know, by construct, an EV, it's a relatively… it's a lot of override to do the serialization serialization, as opposed to a tap, where with Apache RO and the IPC RO, The overhead is relatively small, because there is not really a deserialization or serialization.
But anyway, we decided to create a third, state where we have this Pseudo-unarialized, even if we know that there is no, deserialization, really, with the… with this format.
So… introducing an arc mutex that will transit across the pipeline, where every element could potentially interact with this mutex.
Is it really, the good approach, because that complexifies a lot, in my opinion, the system for an optimization that is not necessarily the true optimization was the OTLP.
We did this, this search stuff regarding OTAP, But I don't think it's, it's a… So great that we need to enter into this, complexity of communicating and architects.
So, my conclusion is, and let me know if you disagree with that.
My conclusion will be, okay, let's go back to a two-state Approach instead of a street state.
we have either OTLP bytes, or the, OTAP, or record Where everything is already… In a s… In a state where we don't have to go back to the state of the receiver to decode the message.
**albertlockett** 35:51 Yeah, that makes sense to me. I'm glad I checked, because I wasn't sure how attached we were to that, like.
no deserialization OTAP to OTAP pipeline, so if that's something we're not very attached to, which it sounds like we're not, then, yeah, let's just have…
**Laurent Quérel** 36:08 For OTLP, for OTLP, I will not say the same thing, but for that…
**albertlockett** 36:13 Yup.
**Laurent Quérel** 36:13 Because another, another consideration to take into account, we, we know that the number of scenarios where This optimization really better.
is relatively smooth.
You have to… to… To… that the pipeline has to… Integrate only a very sole subset of processors that does not require to do this, ultimate transformation into the, auto power recorder.
So the, the retry processor, the… the routing, the signal, the type… I can't remember the name of this thing, but the router by, signal type.
But after that, there is not so much type of processor that doesn't require this transformation.
**jmacdonald** 37:09 Yeah, because if you're gonna send that OTAP payload onward, you're gonna re-encode it almost certainly in a new stream with a different… with a different producer, I think.
I can't see when you're gonna just forward those bytes.
**albertlockett** 37:26 That… is a good point.
**Laurent Quérel** 37:28 Yeah, that's a good point.
Definitively, yeah.
**albertlockett** 37:32 Yeah. Okay, cool. So that's, okay, so that makes, that makes things a bit more, a bit more straightforward then. So we'll just do the deserialization in the OTAP receiver, forward it as arrow record batches, and Okay, cool. Yep.
That works.
Glad, glad we asked, because I had… I had done it the other way, and I was like, this sucks, so… Yeah.
**jmacdonald** 38:03 Yeah, this was maybe a question I had stuck in my head, was that I remember early on feeling, you know, years ago, that the hotel aero Data stream had some sort of, like.
state in it. And of course, later, I was pleased to learn that all the state is located in the consumer producer. Once you get your arrow record batches out, there's no more statefulness in it. And I guess I had maybe suppressed that concern when I saw the OTAP Bytes representation.
Now I realize, like, the logical error there, too.
**albertlockett** 38:41 I had spaced data on that as well. I should have realized when I was reviewing all Jake's IPC stream stuff that that would have been an issue, and just… Okay, cool.
That's solved.
**Laurent Quérel** 38:54 Cool. Can share my screen very quickly.
So the PR… what is the number of this PR? Let me check.
**jmacdonald** 39:17 It's 1… 10.33.
**Laurent Quérel** 39:19 Okay. So just, a quick… Let's put that outside.
the… the big picture of what I'm trying to achieve, and the intermediary step, step.
So, we have those, pipeline engine, the executors, PIN2Core, We have this, local controller.
There is already, APIs.
In the previous year, we had a set of APIs to get metrics and aggregating metrics.
And the goal there was to… to build, an observed state Where… that will be updated, basically, with observed events that are emitted by either the controller or each individual pipeline engine.
And… and those, observed events represent, okay, my pipeline is running, is pending, is, is stopping, is blah blah blah, so there are multiple Type of, or my pipeline is draining, meaning that we start to… The shutdown procedure, and we are progressively consuming the remaining messages into the queues, making things clear, and without losing any data.
So the goal was, being able to have an observed state.
Per pipeline instance, and a global, let's say, a global representation of that. So, with some logic. So, the entire system is running if at least one of the pipeline instances is running.
That's an example of rule. Or we have an issue if we have at least one issue in one of the pipelines.
So it's very similar to… I took the… I basically reused the… the concept and the… the observed state model used by Kubernetes, and adapting it to what we have to have something that, on which we could rely for the Phase 2, Which will consist to, To support live updates, or live configuration, by comparing what we want to achieve with what we already have.
So a quick demo.
I'm always… oh, okay.
I never understood why the stop sharing button is… You never know where it is.
**jmacdonald** 42:06 Ugh.
**Laurent Quérel** 42:07 Okay…
**jmacdonald** 42:11 What gets me is that when you're presenting, you can't put your own hand up, and like, I'm presenting and someone else is talking, and I want to put my hand up, and I can't.
**Laurent Quérel** 42:19 Oath.
Let's see, shh… - How do I use it?
doing some, cleanup on my screen. I have so many things. And for this, next step, I need to share be onto your screen.
Sorry, sorry, it'll be too long.
Okay, back… Okay, can you see my screen?
There's a terminal on the left.
Yeah, that's okay.
Yeah, so the goal will be for me to show you the new infants.
And what happened to the states when we start the system, or when we kill… let's say we shut down pipelines.
So let's start the… I will start it with… So we have now this, also, new option to define, core ID range.
the goal was to, to help freeze, segments, let's say, to split the cores for different elements of the benchmark infrastructure. So, for the generator, we'll go in, let's say, core 1 to 2, the system under test from 3 to 5, and so on.
So that we know that we have a minimum of perturbation, for the different elements of the benchmark system.
Okay, so, running… Okay, so… This system is listening to the port 8080 by default. By default, so we have this, new pipeline dash groups slash status.
And, providing, an aggregated view And a detailed view per core.
So we know that each of the pipelines running there are running.
There is, the, the… The orbit mechanism does not yet exist, but we already have, we derived it from the few events that are already integrated, but the goal will be also to have an orbit mechanism so we know when something is no longer responding for whatever reason.
So now, if… I… send this, post method, which is pipeline group slash shutdown with a post, So we receive… The fact that this command has been accepted, so it's a 202.
Nothing happened there.
But if you… If you look at… The statues, now all the pipelines are stopped.
And it's not because I updated directly the observed state when I received this message, It's more because… I send a shutdown to all the pipeline, and those pipelines in reaction.
Starting to, to drain the pipeline.
And, once their, instance is dead, the controller detects that and updates and creates an observe, event message, saying, oh, by the way, this pipeline is stopped, and then we update this, this thing.
So, nothing really fancy, but, that could be, helpful.
For debugging and troubleshooting to begin, right now.
Yeah, that's it.
**jmacdonald** 47:21 It sounds like your vision is, the reconciler concept. I feel like maybe we haven't learned enough about it yet, but, it reminds me of Kubernetes.
Just…
**Laurent Quérel** 47:32 Yeah, that's, difficult.
**jmacdonald** 47:33 The configuration and wait for it to heal.
**Laurent Quérel** 47:36 Yeah.
That's definitively the source of inspiration.
**jmacdonald** 47:40 No.
I look forward to seeing how that gets implemented. It's one that's interested me.
I'm looking for abstractions and… Libraries that do it automatically, or ideas about doing it automatically.
**Laurent Quérel** 48:02 Okay.
**jmacdonald** 48:03 Done our demos.
**Laurent Quérel** 48:05 Yes.
So, otherwise, we have the P data and the batch processor that is, Close to the, to be done.
Few optimizations have been, few fixes and optimizations have been done last week by, Albert. David is integrating the… work from Michael and Albert. I think, David, you have been able to fix your issues.
Okay, so, I think we are in a good shape to have the batch processor, Oh.
**jmacdonald** 48:46 David's muted. I'm muted, too.
**Laurent Quérel** 48:52 Okay.
Is there any other topic that we'd like to discuss?
**David Dahl** 49:00 Oh, sorry, can you hear me now?
**Laurent Quérel** 49:02 Yes.
**David Dahl** 49:03 Oh, I apologize. Yeah, Albert really, figured it out from the Git standpoint. Thank you, Albert. And, you know, at any point, if you can… it looks like it's ready for the merge queue.
So… And then the next stuff is internal telemetry that I'll be adding to, several processors, so… Exciting stuff.
And thanks.
**Laurent Quérel** 49:25 Nice.
Cool.
**jmacdonald** 49:27 Yeah, the batching logic is very sophisticated, but I think this is the power of the arrow representation. Like, sure, we're gonna get more complicated batching.
But I'm… I'm pleased and looking forward to it… seeing it.
**David Dahl** 49:39 It'll evolve, for sure.
**Laurent Quérel** 49:44 Yeah, what is not yet, definitively supported is the… what you did, Joshua, regarding the header and the ability to use some metadata?
This part is not yet integrated into the batch processor.
**jmacdonald** 49:59 And that will tie back to our question about context.
Which I think we should leave open, since I don't have any new thoughts.
**Laurent Quérel** 50:08 Yeah.
Book it.
**jmacdonald** 50:13 I think we're done.
**Laurent Quérel** 50:13 Do you have anything to, to discuss…
**Chris Hain** 50:18 No, nothing particularly interesting.
**Laurent Quérel** 50:22 Okay.
Sounds good. Okay, so I think we can get back the last 10 minutes, except if we have… urgent a bit.
**jmacdonald** 50:31 Thank you, I'll see you soon.
**Laurent Quérel** 50:32 Go to…
**albertlockett** 50:32 Excuse me.
**David Dahl** 50:34 I don't know.
