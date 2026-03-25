SIG: Collector SIG
Date: 2026-03-25
Duration: 20 minutes
Zoom Recording URL: https://zoom.us/rec/share/nAQKhTsS5gRuVwIzt1q2U8aisA9zVsW-0EP-Dt-Y9Uh1_C-hVkT8Hps2Lz9n5QkC.jBZ143705iVGGj-O
============================================================

## Zoom Recording Transcript

**Andrew Wilkins @ Elastic Observability** 02:31 Hey, Blake.
**Blake Rouse** 02:33 Hey, how's it going?
**Andrew Wilkins @ Elastic Observability** 02:35 I bet. It might just be you and me.
I think everyone's at KubeCon.
**Blake Rouse** 02:40 Yeah, I was wondering how many people were actually gonna be here today, but keep going.
If anyone's gonna actually show up today.
I'm just trying to get awareness for my RFC for partial reload. Still trying to get some… Some eyes on it.
**Andrew Wilkins @ Elastic Observability** 03:02 Likewise with my… RFC for the scraper controller.
**Blake Rouse** 03:12 What do you… how do you normally, like, get people to, like, Actually look at it.
**I got, like, brought it up, like, multiple sigs, multiple times, and just… Andrew Wilkins @ Elastic Observability** 03:22 Yeah, I think that's the way.
bring it up on the SIG meeting.
Regularly, as if needed, and… Otherwise… I guess, figuring out who the people who might be interested are, and… ping them on the CNCF Slack.
Yeah.
**Blake Rouse** 03:43 We might have to start going down that route. I haven't pinged too many people directly, but maybe start with that.
**Andrew Wilkins @ Elastic Observability** 03:50 Hey, Josh.
**jmacdonald** 03:53 Hello, hello, hello.
**Andrew Wilkins @ Elastic Observability** 03:55 There you go.
**jmacdonald** 03:56 Here we are.
Hi, Blake. Hi, Andrew.
**Blake Rouse** 04:00 How you doing?
**jmacdonald** 04:05 Alright.
It's KubeCon, so it could be a quiet meeting, but I, I know I try to make it every 3 weeks.
just got out of a meeting a minute ago, so here I am.
I had put something on the agenda.
mainly it's procedural. I'm supposed to do this. Talk about this at a meeting, and… This is the next meeting I have.
So I would be glad to talk about the thing on the agenda. I could even share the notes.
And then I'd be glad to talk about… It keeps happening.
There it is.
My calendar has a bad invite, but I would be glad to share what I see.
Here it is.
Cool, well, should we go through a stability phase on the board? I don't ever do that.
**Andrew Wilkins @ Elastic Observability** 05:05 Maybe just have a quick look.
I did have a quick look earlier. A lot of.
**jmacdonald** 05:09 Fantastic.
**Andrew Wilkins @ Elastic Observability** 05:09 are assigned, some of them need discussion, and I don't personally.
**jmacdonald** 05:13 Guestion needed, okay.
**Andrew Wilkins @ Elastic Observability** 05:15 Have anything to say on them.
Yeah, like, there's maybe lines… so these… the top four, all need discussion, and I… Don't.
Really have anything to do with those components, personally.
**jmacdonald** 05:31 Right. I feel like we discussed this once here, but maybe not with you.
I don't remember having an opinion on that one.
**Andrew Wilkins @ Elastic Observability** 05:41 Yup.
One… Line 6, host metrics receiver deprecation could be picked up by anyone, I imagine.
**Almost everything else is assigned already, so… jmacdonald** 05:59 Never stale.
Oh, I see.
I do not feel qualified to start fiddling with this board, to be honest.
**Andrew Wilkins @ Elastic Observability** 06:12 Yep.
**jmacdonald** 06:13 Wow.
**Andrew Wilkins @ Elastic Observability** 06:14 I think it's more like a, I guess, a bit of a call to action for people to pick things up.
**jmacdonald** 06:19 Right, Host Metrics is also on the top here, Alright… Oh, dear.
This is old.
Okay, I don't have an opinion.
**Andrew Wilkins @ Elastic Observability** 07:09 Alright, how about we just move on from this boy?
**jmacdonald** 07:12 Sorry.
Sorry, the… I would be asking, Dimitri questions about some of these scrapers. I know he's got much of the answers often, and actually you, Andrew, so… Yeah, especially.
**Andrew Wilkins @ Elastic Observability** 07:30 the entity refs stuff, I think Dimitri's probably the person to talk to about that one. Line 5.
**jmacdonald** 07:39 Yes.
Okay. Beautiful.
**Andrew Wilkins @ Elastic Observability** 07:43 Pick it up next time.
**jmacdonald** 07:45 Next time, next time.
Well, I hope that wasn't disappointing.
shall I just walk us through this, since it's procedural? I said I would do this at a SIG meeting. Of course, it's two people I'm talking to, so it feels kind of silly. This PR has approvals. I've been working on this for a long time, because you see, like, there's an older PR that I opened, like.
Last year, this time.
Or… It follows one of these.
that I opened last… I don't know, September. Okay, so that was my first try, and then before that, I tried it Again, so this is my third try.
From June.
And the way I tell this story is that, when I started working on trying to think about limiters, and I basically faced so much, like.
this is going to be really hard now, that I didn't get much further, and I apologize for anyone who was hopeful that I would make more progress. But I did learn about some of the opinions that people had about How we write interfaces for the collector so that they are stable and long-term commitments.
And give us room for future expansion.
And so this is the document, and I… I would describe this informally as a technique that I discovered when I came here. As far as I can tell, Bogdan is the one who created it.
And as far as I'm concerned, it's great. So it's a good pattern. I think that there's not enough documentation on the go for how to make stable long-term interface commitments, and hint, hint, gRPC could do more of that. So… so that's this document, has been through quite a bit of review. It's mostly human-written, I would say, mostly. I don't write tables as much as this, but that's the idea.
And so this is just, like, spelling out the style that you see, kind of all over the collector. It's not just for the extension point interfaces that we have, it's also for things like the config type and the factory type, and it's sort of pervasive in our codebase. So this is kind of trying to give it a document After explaining this sort of… sort of whole thing, we talked about there is some precedent there, out there in the Go community for this, but it's not very well documented or known.
Talking about sealed and open interfaces, which is one of our major levers for controlling interface evolution.
And then… and how we use… Also, they're called optional in the collector. You don't have to implement something, therefore it's optional.
And this is… but for sealed interfaces, if you have a private method, nobody else can implement that, and you need to use constructors, therefore, or you need to use embedding, and those are sort of the two techniques that we know of to make safe evolution of interfaces. One is to use an embedded like, no-op struct, and that's how the Go SDK goes. For the collector, we're more interested in these no-op functions, so you'll have a constructor that takes functional arguments.
Expressed through these types.
These types are function types like this.
And then you can have functional options and mix them in together.
This just says, you know, like.
for example, middleware extensions, we are ready to add a new middleware extension for a new client RPC. I imagine one called Super, so you could have a super client options, and you could have a gRPC client V2 if they decided to change their option struct or whatever. So the idea that you can extend these interfaces.
And then we have some conventional patterns, like testing and no-op implementations.
And there's some examples, and that's really it. I put a link to the… this and a few of our important RFCs. I didn't want to single my own out.
So I think these are my top 4.
That's it.
**Andrew Wilkins @ Elastic Observability** 11:55 Right, and just so… just to make sure I understand, you're saying this is essentially formalizing things we're already doing?
**jmacdonald** 12:03 Yeah, it is. I would say that if you look closely at the code, it is… 90% accurate, and there are some accidents.
Places where it's not fully extensive, in the sense, like.
If you look at the factory configuration, you have a base factory which has The component type and the… or ID.
And it has… capabilities, I think, or it has a default config func.
So, like, not every argument is a functional type, because we have these constants and literals, and I left out a little bit of variation there, so… If you have a factory, there is a… You pass in a type func… you don't… you don't pass in a type function, you pass in a type.
And so there's a little bit of inconsistency there, like, around how that base factory works, but otherwise, it's… it's almost complete, and I think when Bogdan was telling me, like, you should go add a no-op test and a test function. If you're going to have an extension, you should have a test package that does this and this and this. Like, this is the document that sort of says this is the standard pattern you're going to follow.
**Andrew Wilkins @ Elastic Observability** 13:25 Yep.
**jmacdonald** 13:26 this.
**Andrew Wilkins @ Elastic Observability** 13:26 Sounds good.
**jmacdonald** 13:27 This is.
And like any rule, there will be exceptions, I guess, but I would recommend that we try to stay on this rule.
And… that's it. That's it, really.
**Andrew Wilkins @ Elastic Observability** 13:43 Alright, thanks for walking through, I'll… I'll try and review it.
Soon.
Did you say you already have reviews on it?
**jmacdonald** 13:49 I have reviews on it. It's been in review and approved for a bit. I re-emphasized this recently when we found bugs in the HTTP middleware, so I don't know if you noticed recent fixes. I can probably find them right here.
was, like, this was viewed as a bug fix, but we could have used an extensibility motion to, like, oh, we have an old bug, like, we're not going to break your interface, we're going to add a new extension. We decided not to add a new extension for this, like, bug of ours, but as I was ironing this out. Like, again, the pattern is that we do something, and Anyway, what's the actual change here?
is that… We have a wrap… Originally, we were returning a bear function, And now we're returning a… function, and we take the context, which we weren't before. Anyway, the point is, like, we were trying to, like, refine this, and we don't have a document saying what our pattern is.
Okay.
**Andrew Wilkins @ Elastic Observability** 14:55 Sounds good.
**jmacdonald** 14:56 So, thank you.
**Andrew Wilkins @ Elastic Observability** 15:00 Speaking of RFCs, I didn't put it on the agenda, but I have that, RFC for adding an interface Or, scraper controllers.
**jmacdonald** 15:12 Yes.
**Andrew Wilkins @ Elastic Observability** 15:13 extensible scraper control that's been open for a while. Do you have any… advice on how to move that forward, and also Blake has something.
**jmacdonald** 15:23 I don't have the number, can I… Andrew Wilkins @ Elastic Observability 15:28 I'll fund it.
But it's… I've brought it up a couple of times in the SIG. It's about… here we go.
**jmacdonald** 15:38 Yeah.
**Andrew Wilkins @ Elastic Observability** 15:39 It's 14469… oh, you got it, alright.
**jmacdonald** 15:42 Yeah.
**Andrew Wilkins @ Elastic Observability** 15:43 Yeah. So, any advice on how… These… this should be moved forward.
**jmacdonald** 15:53 Huh.
this… this link here was the formality that I just went through with my RFC. So one thing you could do is present this RFC right now.
**Andrew Wilkins @ Elastic Observability** 16:03 Oh, no, I've already done that.
**jmacdonald** 16:04 Okay.
**Andrew Wilkins @ Elastic Observability** 16:05 I mean, do it again, but… jmacdonald 16:08 I actually read through it, and and… I… the only way I can answer that question is that I do go every Monday to a meeting that is the wrong time for you.
And see the maintainers usually, and I would be glad to, push that for you on the coming meeting next week, I guess.
**Andrew Wilkins @ Elastic Observability** 16:34 If you would, that would be much appreciated.
**jmacdonald** 16:36 Okay, I will.
**Blake Rouse** 16:38 Would you be interested?
**jmacdonald** 16:39 what I'll do is… Blake Rouse 16:39 mine as well.
**jmacdonald** 16:41 Do you have an RFC, or is it a particular… Blake Rouse 16:44 No, it's an RFC, the Partial Reload RFC.
**jmacdonald** 16:46 Oh, yeah, yeah, yeah, okay. Okay.
**Blake Rouse** 16:50 People to review that one, and it just… it just sits there.
**I think last time we met, you were like, yeah, everyone go look at it, and I… jmacdonald** 16:58 Did I? Did I do that? Yeah, of course I did. You said that.
**Blake Rouse** 17:01 You didn't go look at it, but you said that.
**jmacdonald** 17:04 Well, I might have looked at it, and then it was one of those tabs that got lost in the great tab blood of… Blake Rouse 17:10 I know how that goes, I totally understand.
**jmacdonald** 17:12 No, it's okay.
Well… I will do that for you guys.
Remind me… There we are, okay.
**Andrew Wilkins @ Elastic Observability** 17:28 What's the meeting, by the way?
**jmacdonald** 17:30 This is the… And this is a maintainer stability meeting. It's like a… Pablo runs it, and it's… it's… I was added to that group when I became an approver.
And I… as you are, I would assume that… I don't know, I don't know… I don't know who is on the invite list now that I realize it, but I feel like you should be there if it weren't in the middle of the night.
**Andrew Wilkins @ Elastic Observability** 17:52 Yeah. Yup.
**jmacdonald** 17:56 It is Monday, 8 AM Pacific.
**Andrew Wilkins @ Elastic Observability** 18:00 Sounds like the middle of the night for me.
**jmacdonald** 18:02 Yeah.
**Andrew Wilkins @ Elastic Observability** 18:03 Yeah, I don't know, I probably wouldn't, but yeah, if you're willing to bring these things up, that would be great. Otherwise… If there's any way we can do these things async, that would be… that would be great for me.
Just otherwise I'll… I'll basically never be in such a meeting.
**jmacdonald** 18:21 Yeah, okay. So… To do my part then, what I'll… what I'll agree to is that your PR is 14469, and Blake's is 14,640.
Oh, and I will… I will plug them, on the Monday meeting that happens next.
And Blake.
I won't do it twice. I will… I have already approved Andrews, and I will approve this one as well, but I'll bring him up at the meeting to help out.
**Blake Rouse** 18:53 Okay, thank you, I appreciate it.
**Andrew Wilkins @ Elastic Observability** 18:55 Yeah, thanks, Josh.
**jmacdonald** 18:57 Okay.
Well, now I've made commitments. And… I did actually read this one, so I will keep an eye on it, and probably approve it for you again, because it always helps to have more of those.
So then what I'm gonna do is… Sure. Oops.
**Andrew Wilkins @ Elastic Observability** 19:21 The only other thing I thought might be useful is if I put together a demo of… How it will actually be used.
But I don't know if anyone's actually gonna watch it or anything, so… I don't know. Maybe we'll just go with a… go with what you're gonna do already, and then if that doesn't… take hold, then I can.
**jmacdonald** 19:41 I mean, I understood, like, the web… the webhook kind of use case and stuff. There were… there were some examples in the… And then… But yeah, if sort of the question is, can we approve this? And then the next question is, how do we help people in time zones that are not 8 AM Pacific?
get their work reviewed and heard, and I appreciate that.
Is a problem.
So… I'll do something. I'll try.
**Andrew Wilkins @ Elastic Observability** 20:15 Thanks, Josh.
**jmacdonald** 20:16 Yeah.
**Blake Rouse** 20:17 Yeah, thank you.
**jmacdonald** 20:19 Well, I won't… talk any more about these, because obviously I didn't read your thing, Blake since the last time, but Yeah.
I guess I would say I have nothing further to say right now, and someone just walked in because it's 5PM here.
**Andrew Wilkins @ Elastic Observability** 20:40 I don't have anything else, so… Blake Rouse 20:42 I don't either.
**Andrew Wilkins @ Elastic Observability** 20:43 Finish there.
**jmacdonald** 20:44 Thanks, and, see you, I guess, 3 weeks from now here, and otherwise online.
**Andrew Wilkins @ Elastic Observability** 20:50 Cool. Thanks. Have a good evening.
**Blake Rouse** 20:52 Thanks. Bye.
