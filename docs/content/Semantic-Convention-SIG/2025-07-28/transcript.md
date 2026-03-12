SIG: Semantic Convention SIG
Date: 2025-07-28
Duration: 61 minutes
Zoom Recording URL: https://zoom.us/rec/share/gooQ3TdfS7Dk6GSqIAt7OQoLpNS-CYTutWWIquq8idl1kf0mb2KwTOJONEwUnTDa.uoHF3efNIKtzBHvn
============================================================

## Zoom Recording Transcript

Christophe Kamphaus 00:00:30 Hello!
Valentin Zakharov 00:00:37 Hello!
Joao G. (Dynatrace) 00:00:52 Let's give folks a few minutes to join.
Then we can get started if you didn't already. Please add your items to the agenda to have. Do you have any?
I'll move the topics from last week that we didn't get through to the top of the this.
so we don't forget about them.
Hope. That's fine.
Alright. I think we have a lot of people so we can get started.
Oh, I'll mention again there was items. Let me share my screen. Then 1st I moved the items that wording next up here. I I imagine that those supposed to be at the top of this because we didn't get to them last time.
Well, so they're here.
So let's 1st look at the triage board for for some minutes.
Oh, we'll put this for more approval.
Okay, this one moves the hardware metrics to. I think Alexandra is not here today.
But I I had my my list to look at this. Didn't have time, but I'll try anybody wants to say something about this. I think this is just moving right. The the one of the last pieces of moving hard coded things to Markdown. Right?
Not much to to say about this.
All right.
I'll take a look later.
yeah, this Pr, here. I had the proof before, but I saw there was some changes.
and I think there's a a question about such things in the agenda.
From James is this related to this Pr. James or.
James Thompson 00:04:05 It's related to that that Pr. And the couple of other documentation related stuff.
Joao G. (Dynatrace) 00:04:12 yeah, I, I looked at it. Weekly. I think one thing that I can mention already before we get to that point.
is that it's best that it does changes to only that have a that has a small focus. Because, I think the changes that you want to have for things that are missing. The the red means that are missing are are pretty good, and those are pretty.
non controversial. So those could could be merged really easily. But I saw that you moved some other stuff so that those need approval from the seek now. So basically, this Pr is basically blocked because it's let's say it's doing more more things than it could do. So if you if you focus the changes in smaller increments, and then they can probably get moving faster. There's just 1 1 recommendation only.
James Thompson 00:05:09 Yep. So part of my problem was those ones that got significantly moved.
We're like for City, for example, sitting under General right?
You don't find it under general right. That's part of the reason why I moved it.
Joao G. (Dynatrace) 00:05:26 Yeah, but then we can we can discuss this more more things more involved things separately. So so you don't you don't feel blocked in your Prs.
because I'm not sure about. Oh, yeah.
Liudmila Molkova 00:05:38 From my perspective. It's just waiting for mobile approvals to take a look because it touches their files.
Joao G. (Dynatrace) 00:05:45 Yeah, yeah, exactly.
But the rest of the chains are very easy. So yeah, good. You you can think, think this way next time. Maybe that helps Okay. So let's see if if the mobile teams react to this. Otherwise maybe we try to reach to some of the folks into directly.
Liudmila Molkova 00:06:12 Now can we move it to a waiting call? Donors approval.
Joao G. (Dynatrace) 00:06:17 To the staff, hearing to, yeah, yeah. Sure.
Liudmila Molkova 00:06:24 You just drag and drop the clean up of docs in the needs. More approval.
Joao G. (Dynatrace) 00:06:28 You want to move the that's true. Yes, we can do that. Yes.
Liudmila Molkova 00:06:31 Thank you.
Joao G. (Dynatrace) 00:06:34 this one's about dependency updates,
Josh Suereth 00:06:39 That one I just reviewed this morning. That came in. I think I think it's it's a it's a no brainer. It just. I needed another approval before I can merge it.
Joao G. (Dynatrace) 00:06:48 Okay, then I'm sure we'll get it by Daniel to me. Too cool. Alright. So. Yeah. Block things. I think nothing changed from last time.
Oh, and then, yeah, I won't go to into too much there. But if you're.
Christophe Kamphaus 00:07:07 Maybe the ad guidance and infometric there. The approval from Adriel came in.
I think we can move it to needs more approval.
Joao G. (Dynatrace) 00:07:17 Which one, now.
Christophe Kamphaus 00:07:18 The second one add guidance and infometric for Cicd.
Joao G. (Dynatrace) 00:07:22 Oh, nice cool.
So let's do that, then.
Anything else that you any folks in the meeting have things that they need seek approval or otherwise, we'll just go to the agenda, then.
Alright.
yes. So start 1st with this item here. That was from the last meeting. Jen AI sick will start allowing complex attributes and span.
Liudmila Molkova 00:08:02 Oh, yeah.
Joao G. (Dynatrace) 00:08:03 It's okay.
Liudmila Molkova 00:08:03 Diana did.
Joao G. (Dynatrace) 00:08:04 About this.
Liudmila Molkova 00:08:05 Yeah.
So in generalic, we are defining attributes that will be used both on events and on spans. And they are complex.
We.
So far we only had complex attributes on events, but now the other is merged.
That allows complex attributes on all signals. We are not going to allow them on metrics or and under in some other places. But we are going to allow them on Spence. And I wonder.
what would be the best course of action for the Jenny I seek, we actually would like to allow with certain attributes and spans.
Now we also have a close. That says that if you, if Api does not allow you to add the complex attributes well.
for now you can maybe Jason, serialize it or not, not populated at all. All of this attributes are opt in so we are not allowing something like, if if this, if this pack beef, none of the Sdks would allow to produce complex attributes on Spence for the time being, for the next 6 months at least in stable form, but some might do in experimental shape. And we would like to start using this.
I'm sorry. I it's my 1st meeting after vacation. I forgot everything.
Joao G. (Dynatrace) 00:09:56 It's okay.
So
Liudmila Molkova 00:09:57 The Tldr any objections on allowing them on Spence. In semantic conventions we have some regal policy policies that block them.
Joao G. (Dynatrace) 00:10:07 I think as long as they're opting, anyway, it won't won't be any problem. So yeah, I I don't see any.
I don't have any blockers against it, so we will have do we have already something? Or do we have in mind something to put that although this is allowed in the spec. Now, metrics shouldn't have it.
No, I don't. I don't remember. No, I don't think we have anything like that. But now that the type of merge. Maybe we should edit at some point.
So it's clear clear it's clear that one should not add it, even though it's yeah.
Liudmila Molkova 00:10:47 We have. First, st we have regal policies that don't allow them.
Second, we have some language in the defining attributes that complex attributes are not allowed anywhere but events.
And there is some text in the auto that we recommend, adding to notify users that unless they have to, they should
Joao G. (Dynatrace) 00:11:18 Yes.
Liudmila Molkova 00:11:18 I can draft a pr that would modify the guidance.
Separately from from this monster!
Joao G. (Dynatrace) 00:11:29 Yeah, sounds good.
Liudmila Molkova 00:11:30 And we can take a look. I just wanted to see if we would rather wait for the spec changes to come.
Joao G. (Dynatrace) 00:11:39 Yeah, I think we we don't need to be blocked by by that.
although they will be the prototype prototype kind of requirement. I think, at this point. Since it's already present in other signals should be.
it should be totally fine. So it's not that it's an entirely new feature you have access, we just enable it to other parts of the Api. Okay.
Liudmila Molkova 00:12:03 Yeah, we do have prototypes. They serialized Jason, though.
Because there is no other way we can achieve it.
But yeah, I'll I'll send a separate Pr. And I'll make sure we for to change the policy for Spence.
Joao G. (Dynatrace) 00:12:23 Perfect. Take care.
And okay, this is just a link to the spec. All right. So next item respond from James.
I think this Pr already existed before? Is it any changes now here or.
James Thompson 00:12:51 It's about understanding how we can go about describing the scenario where you either have a Mqt. Broker that you're using to send messages to, and is that is that constituted as a messaging system? Because you're using a broker. You might not know what broker it is, but you know you're using a Mqt broker alright, and similar thing for signalr.
Alright. So there's examples there of using those systems.
All right.
Alright. So it's about understanding what's remaining to unblock this right? Like, it's not talking about the protocol it's talking about when you're using a product as a messaging broker system that you're sending messages to to distribute out.
Liudmila Molkova 00:13:40 Is it a theoretical scenario, or is it a practical one? Do? Do you have an instrumentation that needs it right now?
James Thompson 00:13:47 So we have the health checks right for.net, which which cover Mqct. And that alright right. And I've I've done it in my workplace.
Liudmila Molkova 00:14:00 Is, is there a link to health check instrumentation? Is it up in telemetry project?
James Thompson 00:14:06 It's the. It's not an open telemetry project. It's a separate project.
Liudmila Molkova 00:14:12 Is there a link to it?
James Thompson 00:14:13 Yes.
Joao G. (Dynatrace) 00:14:15 Okay, so
Liudmila Molkova 00:14:16 Go ahead!
Joao G. (Dynatrace) 00:14:17 Yeah, that will. That will help out. Because, Bob, what does the the the health check does it like? How? How? How would it need to to know.
James Thompson 00:14:30 All right.
Joao G. (Dynatrace) 00:14:31 And the serving system. What.
James Thompson 00:14:33 Alright. So so it checks the connection to the messaging system and and can report that result.
All right. So it's about defined having that messaging system defined. It's a similar thing for the database systems.
Joao G. (Dynatrace) 00:14:45 Yeah, okay, so, but the so the these conventions that that we have here in this these messaging systems are to be used on when you produce messaging spans. So what what feels like you you mentioned is you. You have a span that tracks a health check. So that's not necessarily a a messaging operation is just an Http call to to get something, so I'm not sure if you need to include which messaging system even, is is related to this health check.
I'm not sure that's where it's really relevant. It would you would attach the messaging system, attribute to a send up, or to a produce operation to to a receive operation in when you're dealing with messaging systems like in a producer on a receiver. But to me feels like if the use case that you're describing is the this instrumentation is running a health check against to see if the broker is is alive.
I don't. I don't think we need to add this. It would, because it would be the same for a database like do we do the same for database health checks, or for any other type of dependency that you're checking. If it's alive.
James Thompson 00:15:55 Well, then, how do you know what system you're checking against.
Liudmila Molkova 00:15:59 You just say unknown.
You say network protocol name is Mpvt or signaler, and a messaging system. If it's a messaging operation, then messaging system is unknown. Let's add a constant here unknown.
James Thompson 00:16:14 No! But then.
Joao G. (Dynatrace) 00:16:15 Is there like, for example, is there? I don't think we have any conventions about, for example, for health checks because you issue had checks. Request to a lot of different dependency right? And today there is no way to know what actually, you're calling like, we don't have any classification, for I'm calling I don't know like a a database I'm calling a messaging system, checking for some other obscure thing like you just call it. And yeah.
James Thompson 00:16:44 No, but when you have a look@boththe.net and the spring boot health checks, they've all got. The data object are being returned for the health checked, and that's how you can know what you're talking to.
Liudmila Molkova 00:16:58 I think Joe's point is different. Right? So if you're just connecting or sending a ping, it might not be a messaging or database operation.
You just call it whatever. And you say network protocol name equals this protocol name, and I think this is a good concern whether this operations should be messaging quarterly operations. They might be in some cases, but even if they are, you don't set them Qt as messaging system name, because it's the protocol name, and you?
No, but that's not the case. That's not the case. You have an Mqc. Broker.
James Thompson 00:17:32 Right. You are using an Mqtt client right to interact with that broker. That's the system to me.
Liudmila Molkova 00:17:40 It's a system to you. It's not the system to what we consider to be a system. The system is the product, the provider name that.
James Thompson 00:17:50 How do you know? For how do you know for an Mqt. Broker from a client level? Who's providing that end product.
Liudmila Molkova 00:17:57 You don't.
James Thompson 00:17:58 Okay.
Liudmila Molkova 00:18:00 Because the instrumentation this conventions are designed for, as I explained.
Joao G. (Dynatrace) 00:18:05 Anyway.
Liudmila Molkova 00:18:06 Comments by the client library that's on the higher level, not on the protocol level. So can I click. Finish an Mqtt level like Mqp. Level. The the people will do weird things in client libraries. They will buffer messages up and send them later. They will budget them together in one protocol message. So the protocol level instrumentation is not the same as client, library instrumentation, the messaging instrumentation.
So we intentionally define messaging and database and gen AI and you name them conventions as the client level the logical operations, not the physical operations.
James Thompson 00:18:45 And that's what I'm talking about. You. You go to Nuget and you download an Mqt library right? Right? And then that's what you're interacting with.
Liudmila Molkova 00:18:54 You can.
James Thompson 00:18:54 I can.
Liudmila Molkova 00:18:55 Download Http library. You can download Amqp library. You can download signal or library. None of them are messaging system, though.
James Thompson 00:19:05 But how do you describe the broker you're talking to.
Liudmila Molkova 00:19:08 Unknown.
James Thompson 00:19:11 If you don't know it.
But why can't you just say it's an Mqt. Broker.
Liudmila Molkova 00:19:16 Because, you know, you're talking to an Mqt. Broker.
Mqtt is the protocol and the way we design the messaging that system. It's it's a more of a product name.
James Thompson 00:19:27 I understand that there's a protocol for Mqt. Right? But that's different to using an Mqt. Broker right.
Liudmila Molkova 00:19:40 I think I made my arguments, and I don't feel like we are hearing each other.
James Thompson 00:19:48 Yeah, I'm I'm like, I know, there's a difference between protocols, right? But I think we're talking about different things.
Yeah.
Joao G. (Dynatrace) 00:19:58 Yeah, i i i I understand the the the concerns on on both sides. But we have already defined the the semantics for this specific case that you have a messaging a library so in your case, you are mentioning a library that is low level. So like it's a it's a library that only talks in. This is the same as if you would download the library to talk to it directly to a database via I don't know ado.net or something, instead of using entity framework, for example, or any other top high, level thing. So Oh.
the the messaging conventions are designed for for instrumentation and the the instrumentations, or the the if if it's built in instrumentation, or if it's a instrumentation, library, it will know which product it's talking. For example, you added in your Pr. Aws! Sns, so that's fine. I imagine that solace is also fine, because it's a product maybe signal also. But I I.
Liudmila Molkova 00:21:05 Has nothing to do with messaging at all. It's not even yeah. It's designed for messaging. It's just web socket based protocol that.
Yes, yes, so it has no place in messaging dot systems.
Joao G. (Dynatrace) 00:21:18 Yes, but this, too, I think this these 2 are really like, I don't. I don't also agree that this should be here, because then. Yeah, we would need to add a bunch of other things here to the list. This this unlocks, adding other protocols that are also talk to another message system that we add here. So that's not.
Liudmila Molkova 00:21:35 Http. Right?
Exactly. Exactly.
You would be at Http here. Now.
Joao G. (Dynatrace) 00:21:40 Exactly, and it's the same for the database system that we also have the other attribute. We only added that database products. They're not the database protocols that you talk to the database because you could also do that.
bomb.
So I I yeah.
I think in in this case it. If you download a library that talks to Mqtt. And the library has no possibility to know which which messaging system is, talk to them just specify unknown. And I think that's that's the way to go. But if the real use case that you're talking right now is the health check, and that is definitely not the correct place to add this attribute, because that's not a messaging operation, because you have to understand as well that the database, the the messaging system attribute is used by many backends to even identify that that operation is a messaging operation. So if you start stamping this attributing to. I don't know health check things. It it, you know. It might make things a bit more confusing because out of the center health check. Now it's is a a messaging operation which is not not correct.
If you're just simply checking, if the thing is alive, just a ping.
Oh, yeah, I I'm fine adding sns and and solace but the rest I think it's it it goes against with the goal of the attribute. So.
James Thompson 00:23:09 But mats is a clear product.
Joao G. (Dynatrace) 00:23:12 It's also not a messaging system.
Right?
Nets you can. You can use nets is just the the transport. But, like you, you can use any.
James Thompson 00:23:23 She's on track.
Joao G. (Dynatrace) 00:23:24 To transport things.
James Thompson 00:23:26 Nats uses Mpht.
Right. Nats uses Mqt. As one of the options.
Joao G. (Dynatrace) 00:23:36 Yeah, it's a yeah. It's a debate on this. Yeah, we we have to at some point.
make a cut on what we DNA is feasible and and not.
James Thompson 00:23:51 Yeah.
Joao G. (Dynatrace) 00:23:54 I don't know if the others have opinions on on this. yeah, you can.
Raising our. We can continue the discussion on the Pr to not to not block the other items in the agenda.
Josh Suereth 00:24:12 Yeah, I'm a fan.
Joao G. (Dynatrace) 00:24:13 If you, if you.
Josh Suereth 00:24:14 Let's let's discuss. Let's discuss more in the thread about, like, I think.
to recap what you're saying. We need to decide what is a system, what is not a system, and what's a protocol? And what's not a protocol? Mqtt is, I think, the very questionable one that's maybe you could include it. But, the overall message of smaller Prs smaller changes add one system at a time. So we can actually have that discussion would be easier than trying to discuss all 3 simultaneously, or or however many are like being added in this particular. Pr, so let's split the discussion, because I think you have a better argument with Nats is like, Hey, this is an actual messaging protocol that people can use or messaging system people can engage with, that makes sense to represent and has its own thing that you can work with. And then we can have the discussion on Mt. Separately. So I suggest, let's split it, and let's move on, because I think we're well out of time. Box.
Joao G. (Dynatrace) 00:25:09 Yes, exactly.
Trask Stalnaker 00:25:11 The last thing that is.
Joao G. (Dynatrace) 00:25:12 Go that way.
Trask Stalnaker 00:25:12 Mention is just that the James. I don't know if this is, you know, urgent for you specifically but the if it's not, and this discussion could be postponed for a while until the messaging semantic convention sig reboots.
That's another option.
Joao G. (Dynatrace) 00:25:40 Yeah, that's a good point, because whatever we define there, it won't be stable anytime soonish. So.
Trask Stalnaker 00:25:48 And we're change. We're gonna change all those system names now, based on what we've done for database and system names. They're gonna be, you know, qualified, and other aspects.
Joao G. (Dynatrace) 00:26:06 Okay, let's move on, then, to not get caught up in time. So trust there's this one. I think this one is for the trivia, right? So I already probably approved it.
Trask Stalnaker 00:26:19 Okay, great thanks, Josh, that's all. We can move on.
Joao G. (Dynatrace) 00:26:23 Yes, I think we don't really need to hml table, for now we can get get by with the Markdown. Only.
Josh Suereth 00:26:34 Thanks for pretty Trask. By the way.
Joao G. (Dynatrace) 00:26:38 It looks, it looks pretty much the same, or it looks the same. Actually.
Josh Suereth 00:26:41 It looks the same, but it reads better in in Markdown. That's the key.
Yeah, yeah.
Joao G. (Dynatrace) 00:26:46 Yeah, yes. And don't break the website. Build.
Liudmila Molkova 00:26:50 To ask now that you know, what shouldn't we do in the future? So we don't break the website again. I'm not sure I understood what was the problem. Initially.
Trask Stalnaker 00:27:02 I.
Josh Suereth 00:27:03 I know.
Trask Stalnaker 00:27:04 Oh, yeah.
Josh Suereth 00:27:05 You ready? You can't use a Href links because the link rewriter that they have the the hard coded set of python scripts that pulls in our repository and rewrites links to be the open. Some trio links cannot understand them.
Trask Stalnaker 00:27:22 I see. So we can do a, we can do anchors. A, yeah.
Josh Suereth 00:27:28 Or if you want to use ahref, you have to go update their python library to be able to handle those links, to be able to do the translation. I know this because I've had to do that in the past.
and I didn't do it very well, which is why you still have a problem.
Joao G. (Dynatrace) 00:27:44 I thought it was because of Hugo that doesn't understand. HTML.
Josh Suereth 00:27:49 Hugo, I think, also had trouble rendering HTML, but there's it's like a combined thing where they try to rewrite.
Yeah. But I thought it was the link. Anchors were the problem.
Liudmila Molkova 00:28:00 So I.
Joao G. (Dynatrace) 00:28:01 Also thought about the link, but the link inside. HTML, I thought, but I also was confused with the with the bug. Description wasn't clear to me as well.
Josh Suereth 00:28:10 Yeah, they're using Regex to pull out links and rewrite them. And so if you put too much HTML around it, the regex collapses on its own weight and doesn't work. So you have to like manually like work back and forth with those to make sure the it's artisanally crafted. Regular expressions.
Joao G. (Dynatrace) 00:28:29 No.
Right?
Liudmila Molkova 00:28:32 So now A should have in the future, and we do have a check.
Josh Suereth 00:28:38 I would say no HTML in the future.
Joao G. (Dynatrace) 00:28:40 Yeah. No.
Liudmila Molkova 00:28:40 HTML.
Joao G. (Dynatrace) 00:28:41 That's that's what I got as well. Yes, are fine, but if they're inside HTML, then it doesn't work.
Josh Suereth 00:28:48 Yeah, no. No links in. HTML, how about that?
Liudmila Molkova 00:28:53 Well, we have the placeholder, the the anchors, the anchors are fine, that's the only thing that's fine.
and we have a check through them before the release. It's it's a bit too late. But yeah.
Josh Suereth 00:29:08 Yeah, okay. So to be to be clear.
If you make a big HTML block, and you put A's in them that are not anchors that are relative Urls. It will break open telemetrio website.
Joao G. (Dynatrace) 00:29:27 Yeah, maybe at some point we need to fix, because at some point the HTML tables will be coming will become handy, I think. But just.
Josh Suereth 00:29:34 The other thing we could have done is we could change all links to be relative to opentelemetry, I/O and mandate, that if all links are open telemetry. I/O. Links! Then we actually wouldn't have breakage.
Joao G. (Dynatrace) 00:29:48 Because the link checker would pass.
Trask Stalnaker 00:29:51 But the Markdown would B.
Josh Suereth 00:29:55 It'd be very weird. Yes.
Joao G. (Dynatrace) 00:29:56 Yeah, yeah.
Josh Suereth 00:29:57 I'm not happy with the whole scenario here, but I'm just calling out like what the problem really was.
Joao G. (Dynatrace) 00:30:05 All right. Okay, so thanks for fixing it. Trust. And then hopefully at some point we'll take a look at this again.
okay, the next item is also phone task. Recommendation.
Yeah, to capture thread, name and thread. Id.
Trask Stalnaker 00:30:22 So in this came up in the Java Sig. Today we automatic. We have a span processor that stamps thread id thread name onto all spans.
But we're thinking that in our next May that maybe that wasn't the right thing to do.
and that it should be an opt-in behavior.
In our next major version.
So just wanted to verify with this group. If that is kind of the right interpretation given. For example, Http, semcom, rpc. These other simcoms don't mention thread. So therefore it's just like all of the other stuff is opt in.
Joao G. (Dynatrace) 00:31:26 Do you? Is there any reason that was decided to add them by default? Do you remember, or was just? Let's add it.
Trask Stalnaker 00:31:34 I think it dated way way back, even probably to the original data dog code base.
Joao G. (Dynatrace) 00:31:46 Okay.
Trask Stalnaker 00:31:47 Yeah, I don't think we ever really thought.
Too much about it.
Joao G. (Dynatrace) 00:31:51 So no, no actual user asking is just legacy, history.
Trask Stalnaker 00:31:57 I mean, I'm sure it's useful for some people. I'm sure some people like it.
but I personally, I I would prefer not to capture it myself. I think it is not worth the extra bites.
Joao G. (Dynatrace) 00:32:19 Yes, for sure.
Trask Stalnaker 00:32:22 And let it be.
Joao G. (Dynatrace) 00:32:23 Because so so you does this mean that we need to add them to the conventions now and then specifically mark them as opt in, or what? What do you prefer, or just leave it as is.
Trask Stalnaker 00:32:37 No, I mean my understanding from previous discussions is that every all other attributes that aren't mentioned in those some cons are treated as opt-in.
Joao G. (Dynatrace) 00:32:52 Okay.
Trask Stalnaker 00:32:53 And so I don't think there's really anything for that other than that. I told the Java Sig I would verify it with this group so that it wasn't just.
hey, this is what I think.
Joao G. (Dynatrace) 00:33:07 Yeah, I'm just thinking, because, like, you know, if, for example, for Http it's not mentioned there and then.
instrumentation start to add or enable users to opt in, to produce, to to add into them.
should this be defined in the Htp conventions? Because then how can.
Oh, components! Rely on the fact that this attribute may be there or not.
Right? So like if I'm on back end and I I receive Htp stands, and sometimes this day, or sometimes not.
I guess the fact that they're opting already gives no no way to rely on it to be there, I'm just. Yeah.
I'm just thinking in this case. Because, yeah.
if we if we think this way, that everything else is that is not mentioned, can still be added as an opting thing.
but the instrumentations pick a few that they think it's good to add, because for the opting thing to work based. Magician must know about the radar you must have already there the the feature that you have to say. I want this attribute right. It's not the fact that the opting feature you pass the key that you want to capture and then instrumentation just magically does it? It needs to know that how to capture this, and where to put it, which value, and so on.
Trask Stalnaker 00:34:39 It depends. In this particular case, it's it's a span processor. It's a global span processor in the Java agent.
So the individual instrumentations actually don't even know about it.
Although that does create a small weirdness where, like a rule based sampler can't use thread name because thread name isn't added before the span is created.
Joao G. (Dynatrace) 00:35:06 Yeah,
Trask Stalnaker 00:35:07 Which is another reason. I just wanna remove it by default, at least.
Joao G. (Dynatrace) 00:35:15 Yeah. I think for me. No, no problem with it.
Trask Stalnaker 00:35:20 Okay, yeah, we can move on. Thank you.
Joao G. (Dynatrace) 00:35:23 Alright next item James.
James Thompson 00:35:28 Yep. So, following on from the past 2 2 or so weeks of discussions, I've been trying to come up with some visualization Poc. Of what a namespace registry would look like.
So if you can go to the pretty view of that.
Joao G. (Dynatrace) 00:35:44 This this slide that I have open here.
James Thompson 00:35:47 Yep, that's yes. So the idea is.
you ha! And just click namespace where it says namespace the Rpc. Next to namespace.
Right? So the idea is you have. So previously, we spoke about doing the Htp. Page.
I decided to against decide to Rpc, because there was a bit more variety of data.
Right? So what the idea is, when you go to the website, you go to the registry, you select namespace, and then you select what namespace you want to look at. So here you have the Rpc. Namespace, and you can see what attributes are there?
Alright, what events are there? Alright! What metrics! And then clicking on one of those items, allows you to drill down to see the details of that. The idea is all this would be automatically generated.
Alright, right? So here is a detailed poc of what it could look like.
Liudmila Molkova 00:36:49 What would happen with the existing documents on Rpc.
James Thompson 00:36:56 Alright!
Alright! So I would set up redirects right. So if you go to the existing link, right it so.
Liudmila Molkova 00:37:05 I mean, there is a content and the existing documents that is not here. Where would it go to.
James Thompson 00:37:12 Alright. Alright. So if it's General Rpc information. So that information message, that's why I have that information block up the top.
Alright. So that's to bring across that general information.
Trask Stalnaker 00:37:24 Right.
James Thompson 00:37:25 But if it's just general information about Rpc. Would go on that homepage for the namespace. So you go to Rpc. And then you can see all that additional information about it.
Joao G. (Dynatrace) 00:37:36 Let's let's compare more or less quickly, side by side to see what we miss, what?
Because it's hard to know from.
Liudmila Molkova 00:37:44 To. One thing we miss is the per Rpc system view.
It does.
James Thompson 00:37:51 So yeah, I wouldn't remove those per. Those per system views all the rabbit and queue implementation versus Kafka. Right?
This is purely about the base spec I've focused on.
Liudmila Molkova 00:38:06 So then what would happen? So the system. Specific things would remain here in the Rpc.
And everything generic will be in some other folder.
James Thompson 00:38:17 With links across.
Liudmila Molkova 00:38:19 To sources like, if I'm just exploring what's out there for? Rp.
James Thompson 00:38:26 But you you currently already have that with attributes, sir.
Liudmila Molkova 00:38:30 I I feel it would be useful to have the product that covers it.
Oh! But having said that.
I I still think that the the super useful part is the Readme page automating the Readme page, and have, like the everything that you need to know about our PC. In one page with links to detailed documents.
But I don't see why we need this whole namespace folder with all the namespaces we can just templatize the readme page which is already there.
James Thompson 00:39:09 So the way I see it is. If you currently go to the registry, you go to the registry. You have an attributes registry section.
Alright.
Joao G. (Dynatrace) 00:39:19 I know.
James Thompson 00:39:20 You. You have an entities, one right? It's about bringing those together and then adding in events, because currently we're not defining anywhere events alright.
Trask Stalnaker 00:39:33 Can we bring, James? Can we bring them into this page here.
Joao G. (Dynatrace) 00:39:40 Yeah, because that's, I think what Mela mentions right? Because this overview that you have now could be done in this readme page here like everything, instead of just links like this, you could have them somewhat all aggregated in the readme page.
like, if the problem that we're trying to solve is improve the navigation.
Then, let's say people go to to the let's let's actually go to the The website.
Trask Stalnaker 00:40:15 We don't really want people to be like, just go directly to the attributes, right? Like part of what we're trying to get across is, hey? These are holistic conventions, they so a starting place for that
Joao G. (Dynatrace) 00:40:34 So yeah, so I'm on the website now, right so and then I click on specs. I I drew down to Rpc, I'm interested in Rpc. And then this is what we are presented with. So we have spends metrics into this, the the system specific things. And, James, what you say is that we don't mention anything about events right now.
James Thompson 00:40:56 Correct. We don't mention events. We don't mention attributes.
Joao G. (Dynatrace) 00:41:03 The attributes are on the conventions where I use them. For example, here on spans right.
Liudmila Molkova 00:41:10 And we can definitely use a link. Have a link from Readmini on Rpc. To the attribute registry for Rpc.
Joao G. (Dynatrace) 00:41:20 Exactly. Yes.
Liudmila Molkova 00:41:20 Yeah.
Joao G. (Dynatrace) 00:41:24 And then events we also rendered here as the same way as we render metrics and spans, and so on.
So it will be another link here, and.
Liudmila Molkova 00:41:34 We can definitely put the table with that lists, available metrics or available spans or available events without definition. Just the the sum table with titles.
Joao G. (Dynatrace) 00:41:48 Yeah, although it's a bit complicated again, because you also have there. But yeah, I I like the overview that this page gives, because it's not long. It's quick. I can quickly find what I need just looking looking at it.
Yeah. And then maybe to solve the problem. There is no attributes. We can just backlink to the registry.
It is a bit odd that the registries like this separated, that you have to go back and forth. I I agree, as well.
Trask Stalnaker 00:42:17 You. Why? Why do you need to go like I actually don't want people.
Joao G. (Dynatrace) 00:42:21 Yeah.
Trask Stalnaker 00:42:22 Going into the attributes registry. I want people to be like, Okay, I'm doing a span, or I'm doing a Rpc event. And they go into this convention and see the cause. Only there is where we override definitions, and that's the only place where, like the the whether it's required or opt in or things make sense.
Joao G. (Dynatrace) 00:42:46 Maybe. Yeah, it's that's a good point, because here is very, I'd say, very boring the things, because.
Trask Stalnaker 00:42:53 It's also misleading. It's misleading, right? Like, people will just be like, Oh, yeah, I'm just gonna throw all of these on my message.
Right?
Yeah, that's gonna be wrong.
Joao G. (Dynatrace) 00:43:05 Maybe we should even entertain the idea of hiding the registry from the website.
Trask Stalnaker 00:43:08 We've discussed that. Yeah.
Josh Suereth 00:43:11 The registry. We want to eventually get the signals to be part of the registry. It's just the questions that Ludmila has been asking on this Pr. Are the relevant ones for why we haven't done so. All the information we want people to see are in the current Markdown, like the way we want people to view the world and say, Hey, what signals do I make this right here, for example, when we can auto generate this file that y'all is showing right now. That's when we can start auto generating a registry. But like we want to start with, hey.
you're an Rpc. Here's the spans. Here's the metrics. And we want to be able to have like this information about technology, specific and dive ins and that sort of thing. So we're starting, much less aggressive with our auto generation. Right? We're starting with, let's auto generate where we can. And let's start building out the capabilities for registry behind it entities. For example, I'm way behind on this, but that's because I've been focused on some yaml changes which hopefully everyone will love when they drop the the if you look at the registry, and you look at entities right? Entities. We have a set of, I think, 6 or 7 bugs around the entities registry and those bugs are to add this information back into the entity registry so that we can have, you know, resource signals be 1st class the same way you see here.
and when that is accounted for, then the source of truth will move from being this thing to the actual entity area, sure. But we have to do that at scale across all the signals. And there's a whole bunch of questions to solve before we move that.
So I think the 1st thing to say on this Pr is basically this view here that we see for semantic conventions of Rpc is kind of the way. We want people to come into the ecosystem today. Right? We want them to see signals first, st and we want to be less about raw labels and raw attributes and more about signals.
The second thing would be, we have to start answering those questions. And we're being conservative with how we do. So there's a lot of people who come to semcom and use it, and we want to make sure that we don't like completely shift their worldview overnight. We want to be like very methodical with how we approach this or when we do, we need to lay down a breadcrumb trail for them to come back from what they were doing to where we've put new information. So we have. We have to be a little bit more methodical here. This is an area we're actually moving slow is to our advantage. We can take time. We can do prototypes. We can. We can learn But yeah, I would say, from my perspective. I like what you're trying to do. Hopefully, this feedback's helpful.
But let's let's start with treating these new registries as an experiment that we're going to refine. And as we start to get it right, then we start moving things over. But we're not gonna be able to drop this. What? What Joe is showing right now anytime soon, until we start getting all those other things, you know, organized and coordinated.
James Thompson 00:46:15 Yeah. Yeah. And like for me, I wanted to start small. So, for example, the 1st case was events right? But then I'll say, can you? Then the question was, can you make a holistic view of what everything would look like put together?
Josh Suereth 00:46:31 We're yes. Well.
Trask Stalnaker 00:46:34 That. And this help, James, it really did help. Today, I think we made a lot more progress today because we were able to, you know, understand.
Joao G. (Dynatrace) 00:46:43 You have to compare the Yes.
Josh Suereth 00:46:46 And and for for the events. If you see what happened with entities right? The comprehensive list could be. Here's a set of to do's of things we don't know how to solve that. We'll work on right?
That that can be in there, too. But yeah, this this prototype definitely helped us have a much better discussion in terms of what you want to do and and how to get there.
Go ahead, Lamel.
Liudmila Molkova 00:47:09 Yeah, I keep thinking that entities and maybe attributes are special beasts.
If you think about people who would discover, let's say events, let's say they discover Rpc.
Streaming event.
Would they implement it on its own?
No, no, they don't. They need spans as well.
at least in how this events are defined today.
So I still think that the people should land in the page that talks about everything at once right? And this page helps them navigate through different pieces.
So when we create this registries, I I think we should be very cautious because we I don't know what it means to implement one metric, but not this. The the rest of the metrics recommended in this space, so we I would rather us move slow.
Joao G. (Dynatrace) 00:48:14 Yeah.
So if, for example, let's say it, it circles back to the smaller change. So if, for example, we miss that, there's no events or no way to find events, things we could see if we can add the events in the overview page like here.
Oh, and that get. Get that part solved, for example.
Alright, let's see, we have. Still, we only have 12 min or so. So let's continue here.
Yeah. So the the next one. I think we kind of already talked about it.
unless you want to mention something else. James, about the item how to get how to best get documentation. Pr progressed.
James Thompson 00:49:11 No, it's it's just about trying to get those, especially those really small ones, progress right? Right? Because I don't want to go through and do all them, and they just sit there.
especially the small ones.
Joao G. (Dynatrace) 00:49:26 Yeah, I'll I'll try to take a look at the dashboard and see the ones that are there that are small. Then I I'll try to go get those movie if if I can.
Okay, thank you. Then we have the websocket traces topic.
I think Thomas is here. Yes.
TH Thomas Hunter II (Datadog) 00:49:46 Thanks. Yeah, I'm Thomas. And with data dog 1st meeting I've been to. So I no idea what the format is. I am seeing that, I think this, this kind of stuff is supposed to happen through pull requests. So perhaps by next week next week we'll try to have one prepared, but at a high level. We are working on websocket instrumentations. In our digital libraries.
You have some release behind. Like feature flags.
I was looking through the open telemetry docs. I didn't see anything, for websockets seemed like it would be.
you know. It would definitely be great to have this as like a hotel standard, have us be in line with that standard.
So I guess am I right in not finding existing Websocket stuff, or maybe is something that I overlooked.
Daniel Dyla (Dynatrace) 00:50:38 Yeah, I can.
Yeah, I can probably answer that.
there is no current Websocket stuff.
There is a browser focused special interest group that recently started meets on on Thursdays. I would recommend you come to that because I think websockets are, while not only browser, it's very browser, like Tangential related. Right?
Yeah, I I think that would be the the right place to get that conversation started.
TH Thomas Hunter II (Datadog) 00:51:24 Okay?
And So before, would it? Would it make sense for me to create a pr example? Span shapes and stuff before attending that room? You know.
Daniel Dyla (Dynatrace) 00:51:38 maybe I think that group is very like tends to be very event focused. There are some span things that they do like xhr, and and fetch and stuff like that obviously creates bands. But I think in general they want the browser experience to work in an event only sort of world.
So I, before creating a Pr, I would probably go to that meeting and and discuss you know what what your strategy is and you know I I could see it both ways. If you come with a Pr. Nobody will will say that like you, you're jumping the gun or anything like that. I think people always appreciate having something to look at and like an example.
But if you don't, I don't think it's a big problem.
Christophe Kamphaus 00:52:33 Always found it a good idea to come with an issue. So if there isn't a Github issue already, create one and propose what you would do in a Pr.
Maybe give some examples there and then you can discuss that in the Sig meeting.
Joao G. (Dynatrace) 00:52:51 Just trust you have your hand up.
Trask Stalnaker 00:52:53 Thomas. Is there specific instrumentation that you're wanting to build with this like a specific web socket library that you're wanting to instrument.
TH Thomas Hunter II (Datadog) 00:53:10 Yeah, we we have a Java Php implementations for a subset of libraries. Valentine would know Java for Node. We're doing ws for python. We're doing Usgi.
Trask Stalnaker 00:53:24 So yeah, I mean Daniel's recommendation. Is good as far as getting other people involved. In this specific case. Since you're if you're wanting to target like Java instrumentation.
If you can.
you know, propose that instrumentation in the Java repo in the Java Sig in and get those people sort of interested in this topic on board that can also help them to, you know.
drive the semantic conventions from that and semantic convention. Folks are more likely to accept stuff if we have proof of concept, if we have already adopted it in, say, Java.
so in Java I can say that you know we would, you know, accept. We don't require there to be simcom first.st You know it's all it would be experimental. But we could you know, land it, discuss it, and then propose it to Semcom Brayden?
Braydon Kains 00:54:39 The only potential counterpoint to that is that, like Websockets, are like a a unified standard with like an Rfc. That lines it up so targeting like a particular library, might seem like an odd place to start rather than coming up with conventions that line up with the Rfc. That all these libraries also have to work with anyway.
Although I get, I guess, like having an implementation as like a proof of concept for the shape makes sense. Just like, if you're targeting one or the other, I feel like targeting. The Rfc. In general is like more accurate to get like conventions that would make sense across the board versus like, sort of, I worry like you start with a Java particular library, and then you like, target the way, what a specific the standard and you'd come up with like a that's the only thing I.
TH Thomas Hunter II (Datadog) 00:55:33 Yeah, we're definitely seeing differences across.
let me just load the instrumenting.
So so with that approach, Braden, we're like, like, we have an internal receipt for data dog. I could make it known applicable to open telemetry. But where? Where would I put such scenarios.
Braydon Kains 00:55:53 So probably you would open an issue in semantic conventions with the the specific shapes, and I guess having a proof of concept is is good. So I didn't want to like.
Say that. Say not to do that, but the the the way, the the things that you would put in semantic connections. This the the span descriptions, the attribute descriptions like stuff, should link out to like the Rfc. And explain, like how it matches with like the purely at the protocol level.
This is something we had to do in like operating systems as well, like we have stuff that like points out to like. This is what the Linux main pages say about this thing. And this is why we're shaping this a certain way like really tying it into the root protocol. Definition is probably the best way to to move it ahead, because it's kind of hard to debate like this is how the protocol works like it's it's written right there in the Rfc. That is is linked out.
Joao G. (Dynatrace) 00:56:54 Don't say.
Braydon Kains 00:56:54 I would recommend like sticking to that as you start to pitch this.
Joao G. (Dynatrace) 00:56:59 Yeah, the only caveat.
And so I'm sorry. Go ahead. Go ahead.
Daniel Dyla (Dynatrace) 00:57:04 The biggest caveat to that is that there might be some things defined in the protocol that you are like impossible to get from certain libraries when you're trying to instrument it.
But obviously, that's what prototypes are for.
Trask Stalnaker 00:57:18 Yeah, it. I like the idea of doing both kind of in parallel like. Send a Pr with some proposal for that in some Conf. Send a Pr for a library instrumentation. The Java folks can then like, look over there.
And you know, cross kind of validate.
I guess the only other question I have is whether we can sit from semantic convention side, whether we consider this like we're trying to.
you know, send new areas through sigs and get groups of people dedicated to working on them. Cause, it's really hard to just accept all these one off components.
So I don't know what people feel about this particular one. If it's something that we could accept into some comp without a Sig, or whether we would want asked to spin up a sig to work on it, for, you know, a a few months.
Daniel Dyla (Dynatrace) 00:58:25 Yeah, that's that's why I said the Browser Sig, cause it feels like big enough to to have a Sig working on it, but not necessarily big enough to be its own Sig. It's kind of a weird middle ground.
Liudmila Molkova 00:58:38 With browser sick. Cover the server side of it as well.
Daniel Dyla (Dynatrace) 00:58:42 No, no, it wouldn't. You're correct about that.
TH Thomas Hunter II (Datadog) 00:58:45 We have a lot of users that use peer to peer or sorry server to server. Yeah, no browser involved. So I wouldn't.
The browser sync redstone.
Daniel Dyla (Dynatrace) 00:59:00 Yeah, I I guess for the browser sake it's less about like they would drive the whole thing as much as like you may find people who are interested in helping contribute to it and and review it, and such there.
Joao G. (Dynatrace) 00:59:20 Yes, to to wrap up because we're almost out of time. I think. Yeah, you can. You can start with an issue and send calls. I saw that you have a bunch of context in the slack thread with architecture designs and so on. So yeah, feel free to put all of those into the issue, and then we can at least start a discussion. And we also can discuss about this requirement to have a sig or not, and maintenance can express their opinions there. And we yeah, we discussed that in the open, for for histories as well. We go from there sounds good.
TH Thomas Hunter II (Datadog) 00:59:54 Great.
Joao G. (Dynatrace) 00:59:55 Perfect. Yeah, we are out of time. Unfortunately, Christoph, I'll move your item to the next. So we talk it next week.
Christophe Kamphaus 01:00:03 Discuss it next time.
Joao G. (Dynatrace) 01:00:05 Yes, thank you. Have a nice day.
