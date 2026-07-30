SIG: Arrow SIG
Date: 2025-09-23
Duration: 35 minutes
============================================================

## Zoom Recording Transcript

**Utkarsh** 01:44 Hey, Blanche.
**Mike "Blanch" Blanchard** 01:46 Fair enough.
**Utkarsh** 01:48 How's it going?
**Mike "Blanch" Blanchard** 01:50 Good, how you doing?
**Utkarsh** 01:52 Yeah, good.
B… working on… some of the, like, the syslog part within the hourly book.
And some other stuff, just… the foundational.
engine components.
**Mike "Blanch" Blanchard** 02:10 So… About to start work on, like, an arrow… Version of our… query transform engine.
**Utkarsh** 02:20 Nice.
Meaning that it will apply those queries or transforms on the Arrow record patches, right?
**Mike "Blanch" Blanchard** 02:30 It's the hope. Gonna try to use Data Fusion.
**Utkarsh** 02:34 Hmm.
Nice. I got a lot to learn there.
Yeah, in general, I think I haven't… gotten a grasp of, like, how to… I've seen, like, these people send PRs about merging arrow batches and all of that, but I… I don't think I understand that completely yet.
Yeah.
Hi, Josh.
**jmacdonald** 03:06 Hi.
Can you hear me? My camera's not working.
**Utkarsh** 03:10 Yeah, we can hear you.
**jmacdonald** 03:12 Well… I was just looking for, notes.
So, secretly, I always hope for short meetings.
This is, already shaping up to be a good one.
Nothing has been placed in the notes.
I had some questions. I know that there's a big F5 event going on. I had some questions, not expecting really to see Laurent, but the fact that no one has shown up from that company right now makes me think that they may not be.
So… I could speak… We are being recorded, but no big deal. We could talk a little bit about the questions I have that might be interesting to the group here?
I could also talk about the hackathon.
project that I was tinkering with last week.
how does the audience feel?
**Utkarsh** 04:21 Yeah, sure.
**jmacdonald** 04:23 Sure, yes, you'd like to hear me talk about the issues I'm having today.
**Utkarsh** 04:31 Yeah. Yes.
**jmacdonald** 04:37 I won't talk about that hackathon in that case. That's actually what I was hoping not to talk about.
And I will pull up… A branch.
And talk you guys through it.
So… Here we are. Here we are.
We are in a branch that I have just started today. This is like a, like, fifth attempt, hence named Context 5. I'm working to add back pressure in the OTAP Dataflow pipeline.
And I was using, working with the feedback that Laurent had given me about my previous efforts. So, first of all, I'm scaling everything really, really far back, to try and avoid anything unnecessary. So, I've taken out some of the features of my earlier investigations, like The hotel rejected count, or, Error codes, or, some stuff like that. deadlines, for example, not… not here. But he did suggest, First of all, using a bit mask for this field, we're going to call interests.
Or at least that's where we are right now. Interest is a way of subscribing to, like, signals saying, like, I only want X, or I only want an X.
And because these fields, which are kind of, like, propagating as metadata in the context.
are kind of, like, private to the individual components. He also suggested using this com… this, crate called BiteMuck.
Which, lets you have, like, 8-byte data types that can become U-size, or U64, etc.
It's a pretty… pretty stable crate. I don't know, I'm trying it out. Also this thing called SmallVec, which took me quite a minute to figure out. I don't know why I have panic unwind. I'll just show you what I have.
Never mind this. So… I was talking about, the type of data that passes in the context. This is largely copied from Laurent's feedback in my other PR.
So there's a context value which is a U8, Or 8 bytes of U8, sorry. And pod here is plain old data.
Hello, hello.
I'm just… I'm just walking through a PR branch of mine, y'all. I'll just keep talking. So, POD, plain old data.
from that BiteMuck, Great. Lets you cast to and from. So this lets me put some private data, like retry count, into the context.
So Laurent suggested that you could have, like, one or two of these. I chose two, he actually suggested three. I only need one for the retry processor, but the point is that this would be some small amount of space that each component can stuff into the context. When they send, it'll come back to them in the NAC or the AC.
So this… PR introduces the AC message, which is a boxed P data.
boxed so that it's a small object with the data on the heap, because it's going through the control channel. Nothing much to see here. In fact, there's a few open questions. The current NAC message data type in this draft Has a string, a Boolean for permanent, Which… In gRPC, it has a specific definition. In HTTP will be something else, but… but permanence. Context is the data. This is, was the recommendation from Laurent. The data coming back, so if I'm a retry processor, and I send my first request, it'll come back with context data.
I made an option so that I could take it and not get confused. You only can take it once, of course.
Still, still sort of, like, learning how this all works. So then refused is the data that's coming back in the NAC message, so… If I am the retry processor, I will send the message, it will come back to me with this context where I stuffed my retry count and this data, which is the thing we're retrying.
Okay, so, I still haven't constructed a NAC message, that's why this is all commented out.
And I've replaced these sort of placeholders. There's an ID in the placeholder, there's no such thing in our system. If you had an ID, you'd have to, like, implement it somewhere, and I… we don't need that ID at the moment. It might be usable for… useful for observability. Anyway, so it's… the ACC message and the NAC message.
I'm… I'm… this is a sort of placeholder here as well, delayed data saying.
I'm… I'm going to delay this.
in the pipeline, it's neither here nor there between the two components, it's in the pipeline controller. This is all, again, sort of, like.
draft 5, but incomplete. So this is that bitmask that Laurent had suggested. It lets you combine your interests for X and next, and it uses this pretty standard crate, I guess, called Bitmask.
Bit flags?
So… Well, I think this is helpful for me to just keep talking through.
Laurent's idea that I'm following here is to keep the, Pipeline's data generic, so the engine doesn't know the data type.
And that turns out to be kind of an interesting requirement, since the data type, then, is something that we control That controls its own context, so you… the engine doesn't know how the context is represented.
However, he also encouraged me to kind of, like.
like, protect the information that we're using for routing this, like, signal, so if I'm responding with a NAC, I'm going to figure out who that NAC is delivered to by inspecting the inside of the context.
And kind of want to protect you from mistakes, basically. So, What I'm doing here… well, first of all, since we're on screen here, this is the method that you call on your effect handler to delay a message.
We would have to implement that by sending a pipeline controller saying, I want this to be delayed, which will call you back when the timer has elapsed.
So then, okay, so this is, like, new tricks for me in Rust.
This is, like, the first time I've done something like this, on my own at least. So… the effect handler is defined in the engine, but I have specific OTAP pipeline data called OTAP P data, And… I'm gonna implement it Or myself.
in a place where it's… I'm aware of the type. So this is the general trait declaration. It's an async trait.
And when I go into the OTAP data flow crate, I'll actually implement this.
So that should be pretty close.
Oh, gosh.
Tests, don't worry about it.
Just symbol names, okay.
Let me get down to something… Interesting.
Nothing interesting. Nothing interesting.
So, this is the context type. It was already added, but it was an empty reserved for future. This PR, I add a VEC frame.
So, frame is… The bitmask of Interests.
the context data, which is 2 words, or 2 U8s, two U8 arrays of 8 bytes each, and a index into the pipeline control structure.
So that says how to route back to you when you send an ACK or a NAC. It also says what you're interested in. The retry example, processor example is one where you're only really interested in NACs the axe just passed through you, and so some of my questions… I have a few questions written down when I finish walking through this. So I mentioned this new trait called Effect Handler extension that we're only going to implement in a context where we know the data type.
Well, what concerns me is that I have to implement this, like, 6 times, because we have local and shared, and we have exporter, processor, receiver, but then I can implement these, like, subscribe to.
And actually, I don't need to subscribe to for an exporter, but for the receiver and the processor, subscribe to will be the what I've done here, which is to push onto that stack of frames a new frame, saying who you are, your processor index, which is this guy.
The interests that you have, and the context data which comes from the component.
Oh, gosh.
I've walked you through all of my, like, engine changes.
I may as well skim through this. This is the actual retry processor, which I'm in progress with, just, again, to demonstrate the proof concepts. So I've created a type called retry state.
It's a register of some sort. It has a U size field. There's only one of them.
So it defaults to zero retries, and then there's this… I mentioned this type called context data, which is a few words of general storage.
you can do from the retry state to get… and this is where I had to learn how to use a small vec. It's pretty gnarly, I don't know.
whatever. They suggested it. And then from the context data into the retry state, so it's two from definitions here, you just take your value and you use INTO, So then… Through the magic of Rust, of course, you get the right data types, and this small vec does the right thing. So, this is how I say, I have one word, it's my retry count, I put it in the context data.
Then I'm a little bit down… so, the retry processor was, like.
pretty bunch of placeholder for a processor that does something like this, but again, AC and NAC weren't real, and those message IDs were kind of made up.
So, what I've done is delete, like, a whole bunch of code on the left side of the screen, because it's basically being thrown away.
And… and moreover, or more to the point, I've removed, like, all the state, so there's no more data structures in this retry processor. It's only going to use the data that it puts into its own context.
frames.
So, that means you have a much simpler object, and so on.
So then, I'm almost finished here.
This is the… what it looks like to program this component, at least this is my proposal.
So, you're a processor, so you're implementing this process message, this is the process.
implementation of the trait, it's also an async trait, right? So you get called process with a message, it can be either the P data for pipeline data, or it can be the control. So if it's pipeline data, it means you're getting a new request.
So then, what you do is you call the effect handler, this is the extension method called subscribeTo.
subscribe to knows that data type is OCHAP PData, so it knows how to get to that context stack, push a new frame. So this says, we're interested in NACS, I'm gonna take my retry state, make a new one, and go into the context data, and then I'm taking the data straight from the the request I got.
That's a, like, no return value method. It is asynchronous, though.
So then, as soon as you finish putting that subscribe to on the stack, then you can call, send message, and then everything here is, like, boilerplate, and it really worries me, actually. The boilerplate is that if then succeeds, great, but if it's a failure, then I'm either gonna drop the data, or I gotta do something right away. And I don't want everyone to have to write this, so I've got some questions for the group, but I won't go into them now.
So once again, we're handling the data, so forward direction.
You subscribe to for the returns?
call, you send the message, there's some boilerplate that I don't want to talk about that scares me. So then you're now in the second branch of the process call, which is the control message. Control message… You are only interested… the main one that we're expecting is a NAC, So then, what do I do?
Nac is a mutt variable because there's a few cases where I'm going to reply immediately to my caller with another NAC, so in case I am going to reply again with failure upstream, I'm just going to keep that NAC and mutate it.
So, if it was a permanent failure, I'm just gonna call this method called notifyNAC, It's not implemented, really, but it will deliver node control… a pipeline control message, saying to do some… some… back pressure.
If it's, got some… a few error… error conditions, like you don't have context, or you don't have, data.
that would be, returned. Then what I do is I take the NAC… it has context, I take the context, I turn it into a retry state. So then I can check if I've got too many retries. If I've already had my three or whatever retries, I will then fail saying max retries.
I then increment the retry count, it was also mutt.
I then look at the time.
calculate the delay according to the config. Those… this is the config that was already there.
I then put a min or max And I now have a new timestamp. This is… I want to delay this message now until a certain time, because it failed once, or at least once. So then I had some code in my previous draft, which checked the deadline. I took deadline out of this example, so never mind. But we could put that back if there was a way to figure the deadline.
It's based on the next retry time. The Go component here, by the way, does exactly that, this code. It says, oh, I'm gonna retry, but I'm gonna time out first, so I'll just time out right away.
Okay, so then you've passed all the checks, you're not at your max retries, there's no deadline expiration, etc. So now, again, you subscribed to, so this is pushing yourself back on that stack.
And then you call delay message. So this is, again, not implemented, but it's saying, I have this piece of data.
I want it delivered, but I'm delaying it. So, calling your effect handler, now I have some questions here, like.
It seems like it might be more efficient to call the effect paneler with a delay, saying, after this delay, put it in the next queue.
But I don't have a way to do that without Complex stuff won't compile.
It would be easier to send a node, like a destination, but we don't actually have that right here in the code. We have a channel. So I don't have a great way to delay the message without coming back to myself first. So that's what I've done.
There's another node control message called delayed data. It comes back to me right after this much time has passed, or this time on the wall clock.
So then I do the rest of the work, but it's the same call as above, and it has all the same boilerplate below. So I call a send message. If it succeeds, great. If it doesn't, then I have a channel send error, which… from which I can avoid dropping.
I take the inner data out, I look at the signal type, the num items, and then there's this metric stuff. Again, boilerplate, I don't like to see it. That's my whole story.
There's nothing else to see here. I deleted all the tests. They were pretty low quality. So, I've shown you my PR.
I could now tell you the questions I had.
Anyone else like to speak?
My camera started working.
Okay, I'll give you briefly my, my.
**Utkarsh** 21:07 Josh, I had one question, yeah, I think that's a lot of changes, but, so what is that… the subscribe to thing? Could you talk about it again? Like, how does that, how is it implemented?
**jmacdonald** 21:19 So, if you think about… here's how I'm thinking about it. In the Go Collector, you know, you… one receiver calls a processor, calls another processor, calls an exporter, and every one of those, there's one go routine. It's a synchronous call, so you're blocking the caller while you do the thing. And in this thread-per-core async model, that's not happening. We see some data, we put it in the next channel, and we're done.
**Utkarsh** 21:45 Yep.
**jmacdonald** 21:46 In that model, the way we're gonna do the sort of call stack according to the design that Laurent and I talked about, which is largely driven by him, but I like it. I just want to say I like it. So, there's no state in the retry processor. What it does is it pushes its return information onto this thing called a stack.
In my previous… Well, I stopped sharing, but the previous, I need to find the… There it is.
just as a reference point for all you, here's a link to my previous PR, where… Laurent placed a bunch of feedback. I'm working off his feedback in that, PR. So, The subscribe-to notion is the word he used, but it says, I'm handling some data, I'm gonna push it into the pipeline, and when you're done, either an act or a knack, please, here's where I am, essentially. So, subscribing to a return call.
Is like pushing yourself onto a stack.
**Utkarsh** 22:53 I had called it something completely different in my earlier… I had called it…
**jmacdonald** 22:57 With reply to, or something like that.
**Utkarsh** 22:59 So what I didn't get was, like, why are Axe and NAX, like, need… why do they need this special treatment? Like, usually we don't have to subscribe explicitly to other control messages, right?
**jmacdonald** 23:11 Right, I think… so, I'm sort of answering based on a little guesswork, because I think, Laurent does have sort of a vision put together. It's that… this is gonna be the most intensive, like, work that the pipeline controller or that the engine does. It's gonna be one of the most common messages, and there will be, we think, common cases like retry processor, where if it's an ACK, I've literally got nothing to do except maybe some metrics. And then wouldn't it be better if you could just kind of, like, quickly do that wherever you are?
as you're unwinding the stack, you're like, okay, I see that it was an ACK, so I'm looking for someone who cares about an ACK. So we start peeling off the stack until we find someone who cares for an ACK.
And then we keep going. This makes it so that all the data memory used for the retry processor, there's no extra copy of the data. There's always one request passing here and there.
Comes back to you. And then… It only comes back to you for real when it's a NAC, in the case of that retry processor. So I guess it's to save the work And it's… I… so… Right now, I keep referring to this thing called PipelineController, it's in PipelineController.rs in the engine, and it's a fairly straightforward piece of code right now. I think the future vision is that we could plug in maybe more sophisticated logic there, or even have it, like, be a configurable choice, which… which pipeline controller do you want to use? The simple one, or the new one, maybe? And that's where we have all the timer state, periodic timers.
if I mentioned this thing called delay data, I'd put that data structure into the pipeline controller. But the pipeline controller is going to be able to see all the nodes, and will have all the NAC state and all the act state.
And… So, there's some challenges that are kind of addressed, potentially, by a more sophisticated pipeline manager. One of them is that all these NACS and Axe.
Have boxed request data.
So that you don't have a very large node control… pipeline control message, or node control message.
But it means that memory is tied up in the boxes within the control messages. So at some level, we can start to have… imagine some sort of, like, higher level awareness. There… I am the pipeline control manager. I… we are out of memory. I can see that we have some acts.
And so on. Anyway… I have some distractions who are entering pretty soon.
I sort of walked through many of my questions. I think I want to save them for Laurent and the team if… from F5.
you know, high-level questions, do I need to res… if I want to insert a delay, do I have to come back to me just to send onward? Well, yeah, because I have to put… be the one that's… Causing the pressure on the sender, maybe.
But then when I fail, what about boilerplate to handle, like.
as I fail to send to my downstream, because the channel is full, now I'm holding the one and only copy of the data. I should knack… If someone else wants to try resending this, I should knack with the data. It means every time I try to send, I have to handle a failure Either then turn around and apply it to another channel, which can also fail.
But then, eventually, we may have to drop some data. I don't know what people want to do.
I find myself wanting to say the retry processor does not need Axe. All it's gonna do is metric.
But the code that has been written through the team has metrics for the ACK case.
And I understand that, so it kind of makes me want to… have pipeline-level metrics, like, I don't want to have to, every component, have to do this metric stuff for the basic counting of errors and successes.
Yeah, those are my questions.
I think I don't quite understand, I'll just state my own uncertainty.
If, say, the OTL… if you're using, say, the OTLP exporter, and it has a limit on outbound requests.
everything's got a limit. Eventually, the entire pipeline stalls.
And I'm calling sendMessage on that… the same channel.
In an async context.
Do we block the node at that point?
And is that safe?
I can't literally block an async thread, but I can… I can… I don't know how to make the difference between blocking and non-blocking invocations, as I send in my… pipeline component. Those are my open questions. Anybody want to talk?
**Utkarsh** 28:32 So, when you say, like, what is the blocking scenario, like, possibly blocking scenario here?
Because from what I understand from the pipeline setup, we have… let's say we have a very simple three-component pipeline definition. A receiver, processor, and an exporter. All the three of them Have that async function, which will run in a loop, which is the receiver has the receive implementation, processor has the process async, and exporter has an exporter.
And our trade.
It's gonna keep switching among these three.
**jmacdonald** 29:07 Let's say I'm the processor.
And the exporter has… A limit on concurrent requests that it's sent itself asynchronously.
And now… You know, it's waiting for those requests to finish.
They haven't finished yet, so there's no space in the channel.
All the workers are busy.
you're blocked.
And I'm now the retry processor. I've now waited for my retry interval, and I'm here handling this data once more.
The next thing I want to do is put it in that channel, but it's full.
Do I return failure to the controller, there's a higher level controller, or do I block the processor since its outbound is blocked?
And I think the answer is probably no.
We have to… I don't know how to say, I want the retry processor.
That's that send delay… I don't know how that…
**Utkarsh** 30:12 Basically, you're saying, like, blocking versus dropping the data, right? Which approach.
**jmacdonald** 30:16 Effectively, yes. I don't know how to block the data, I only know how to fail and drop fast.
I mean, I think blocking there would anyway happen if you, like.
**Utkarsh** 30:28 In your scenario, the exporter code will somewhere have an await point, which wouldn't be completed, and then your thread might go and look at if the process function can proceed. The process function also hits an await point where it cannot proceed from it will see the receiver function. If none of them can, then basically your thread isn't going to be doing anything at that point, so it is blocked, it's not going to be receiving newer items, and…
**jmacdonald** 30:51 So, do you… is your expectation that send is blocking most of the time when I see it? It's never non-blocking?
**Utkarsh** 31:00 Then… to the channel.
It's… I think we are only using the non-blocking version of send, as in… yeah, we use the send async await, we use the async send, right?
You don't use the blocking thing.
**jmacdonald** 31:15 Okay, so…
**Utkarsh** 31:15 Yeah.
**jmacdonald** 31:16 If there's room in the channel, it succeeds, otherwise it fails.
**Utkarsh** 31:19 Hmm.
**jmacdonald** 31:21 So maybe I'm imagining there's some helper, like, apparatus that says, I'm gonna do a thing on a channel, and if it fails, I might want to do another thing on channel, and if Or I might want to wait, which means sending a pipeline delay message, so you can respond in various ways by trying to send a node control message to save yourself in this moment where the channel is full. So, first you could Send a request to delay. If the node control channel is full at that point, I'm not sure what to do.
You could start backing off, I guess. I don't know. I'm… I'm not… this is the question I have for Laurent. Laurent.
**Utkarsh** 32:03 Yeah. Maybe, I think in our channel, I don't know if we have, like, a try-send.
option, which…
**jmacdonald** 32:09 like, let's just…
**Utkarsh** 32:11 It's a synchronous thing, and if it's able to enqueue something, it returns successfully, otherwise it just says it's full or… From that point, you can maybe take… Amato decisions.
I haven't checked the… I think we will have to look at our MPSC channel, file that I think Laurent had added in the grades.
**jmacdonald** 32:34 Yeah, I was just looking at, I won't share unless you demand it, but in the engine crate, there's a message Which has the local sender and the shared sender combined into a thing called sender.
It has a tri-send and a send.
So, that makes me think send is blocking.
And try Sam.
**Utkarsh** 32:58 Could you share your screen?
**jmacdonald** 33:00 Yeah, okay, alright, alright, alright.
Share now.
It's gonna be Emacs, sorry, y'all.
Here we are.
I am in, the repo OTAP data flow creates engine source, so message.rs.
And this type sender… Is the… if you're a receiver or a processor, you're sending to one of these, and it's whether you're local or shared.
**Utkarsh** 33:27 That you have these two enums.
**jmacdonald** 33:29 So most of the time, when I say to my effect handler, Well, let's go local processor.
Local processor… You say, send message.
It says default sender, which is an option.
**Utkarsh** 33:49 Huh.
**jmacdonald** 33:50 But you can call send.
And then you will wait.
**Utkarsh** 33:54 Yeah, that's the async.
**jmacdonald** 33:56 And if the channel is full, it blocks.
It blocks this process.
**Utkarsh** 34:04 Yeah, you won't proceed further from that, I mean… You will…
**jmacdonald** 34:09 I won't.
**Utkarsh** 34:09 at that point.
**jmacdonald** 34:10 I send, it would return fast to me, and I could handle. Okay, so I don't have to worry about failures.
from… But what's strange, I guess, then, is I'm going back to message, In the engine.
Ugh.
Message, and… I was going to show… No, I can't remember. I'm a little confused by all this.
Yeah, okay. Sorry, this is why I don't share my Emacs.
As I am explaining, many questions. I think I don't have much effort and energy left for this day, and I'm gonna go see whose dog that was. Actually, I know whose dog that was. Thank you all, people. I'm gonna see you all later. You all know how to Teams me.
Or Slack me.
**Utkarsh** 35:23 Alright.
**jmacdonald** 35:24 Thanks, Akash. Thanks, Gokan, thanks a bunch.
**Gokhan** 35:29 Bye.
