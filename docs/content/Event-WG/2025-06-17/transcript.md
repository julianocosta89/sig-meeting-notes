SIG: Event WG
Date: 2025-06-17
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Liudmila Molkova 00:00:53 Hello, hi Austin. Long time. No see.
Austin Parker 00:00:56 Hi.
Liudmila Molkova 00:01:00 Where is everyone?
Austin Parker 00:01:02 I don't know.
I am fighting with slack, dump.
Liudmila Molkova 00:01:19 Hmm!
Are you backing it up for the whole up and telemetry, or for yourself?
Austin Parker 00:01:25 I'm trying to back up like the private channels and like some Dms. But I also have many years of dms on here that I'm not going to get every single individual DM, Id and Plugin. So I guess there's just going to be conversations lost to the mists of time.
Liudmila Molkova 00:01:53 Yeah, are we moving to this court? Is it decided?
Austin Parker 00:01:57 I don't know.
Liudmila Molkova 00:01:59 Okay.
And and let's see if task is joining.
Austin Parker 00:02:17 Trask is also in.
Liudmila Molkova 00:02:20 Slack, dump! Hell right now.
Austin Parker 00:02:46 Hmm.
Liudmila Molkova 00:03:12 we are waiting for trust. Let's get started.
So we didn't have any attendees last week, but we managed to discuss a lot.
Trask Stalnaker 00:03:25 I saw that after the meeting.
Liudmila Molkova 00:03:46 I have a joke trust about your name. It's politically incorrect. I'm sorry. I'll tell you in private.
Trask Stalnaker 00:03:53 Sounds good.
Liudmila Molkova 00:04:01 Okay, it's the 17.th Okay? So we don't have any agenda. Do we have any follow ups on the complex attribute attempt? I'm sorry I'm I'm doing. School runs for 3 weeks, and I'm absolutely distracted with everything, and I was not to be. I was not able to make much progress on and keep up with the discussion.
Austin Parker 00:04:33 I have also been out and I saw there was a top that this Otep came up at spec, but I wasn't there for it.
Liudmila Molkova 00:04:48 Do you wanna take a look? We are asking people to review and give a final.
Austin Parker 00:04:52 Is it? Is it ready.
Trask Stalnaker 00:04:54 Yeah.
Liudmila Molkova 00:04:55 Oh, it's absolutely ready.
Austin Parker 00:04:56 Okay, I I will look after this unless you would prefer me to look at it. Now.
Liudmila Molkova 00:05:03 No, we we we would like to get it merged, but it's not something. I I would imagine it would take us at least a week to get all the eyes on it.
Trask Stalnaker 00:05:20 Yeah, we need more approvals. Right now, is.
Austin Parker 00:05:23 Okay.
Trask Stalnaker 00:05:26 basically, I just wanna make sure that I know there's at least one person who's in the camp of like doesn't really support this, but doesn't not gonna block it.
And I wanna make sure that yeah.
and I wanna make sure that there's So I asked kind of specifically in the spec meeting, like, if other people are in that camp to DM me cause I wanna know if we have.
I wanna make sure we have good community support behind it. Since there is an argument that can be made that this is a breaking change.
So I I started. Yeah, I started looking through the the most recent comments.
So I wanna try to get those resolved and then I'm gonna reach out to maintainers and try to get more check marks. They don't need to be green check marks. We just need to show that there's broad community support for this.
Liudmila Molkova 00:06:55 Where I.
Robert Pająk 00:07:04 I have a logistic question.
It's annoying, but I think it may may help, if Big may have you considered joining some linguistic meetings to take, like to take a look.
Trask Stalnaker 00:07:20 Let me ping we ha! I don't think we've directly pinged language maintainers yet on this.
So let me do that 1st and see if we can get people that way.
Robert Pająk 00:07:35 Yes, that's correct.
Trask Stalnaker 00:07:36 That's a good idea. If we're if we're still in this state next Tuesday.
I like I like that as a follow up plan.
Liudmila Molkova 00:07:46 Robert, can you bring it up in the go or.
Robert Pająk 00:07:49 It's already approved. It's already approved. There's already a prototype.
So it's approved by me and David. You are both maintainers. And yeah.
Liudmila Molkova 00:08:00 Do we want there, like somebody from the seek to actually go and approve the autop or.
Robert Pająk 00:08:07 I think it would be better.
I think, a little better. So, for instance, even there's and you know, Pr. In the in the Python prototype. I think it will be good just to have some kind of brought approval of the prototype.
Trask Stalnaker 00:08:22 I think what Lamilo is suggesting is getting the people who approved the prototype to.
Robert Pająk 00:08:27 Yep, that will be. That will be even better. Yes.
Trask Stalnaker 00:08:31 It's the Otep that I want to see lots of check marks on.
Robert Pająk 00:08:36 Yep.
Liudmila Molkova 00:08:44 Right trust. Can you ask, or Europe?
Are you a Java Maintainer? Do you want to do we need somebody from the Java side, or we will not get their approval anyway.
Trask Stalnaker 00:08:58 I don't think we'll get.
John Watson is just not very involved. Doesn't have time lately to do much.
but I can. I can get Jason to review And let's see anyone.
Yeah, at least, Jason.
Liudmila Molkova 00:09:30 Okay, I can ask C. Sharp folks. See, Joe, is not C. Sharp a pro maintainer anymore? Right?
Trask Stalnaker 00:09:39 Yeah, but he's still a he's a spec sponsor. So his it would still be good to get Cj's.
Robert Pająk 00:09:50 I think that's I think you have. Still, you know, folks from Microsoft, I don't know is my plank chart is still maintaining.net or not anymore.
And Raj, okay, so probably Raj.
Trask Stalnaker 00:10:02 But Raj is.
Robert Pająk 00:10:03 Cheers.
Trask Stalnaker 00:10:03 Out for 2 months.
Robert Pająk 00:10:07 Okay.
Liudmila Molkova 00:10:09 And then, if it gets to just approval, we can.
Robert Pająk 00:10:14 I think I'll you can also ask Alan West from new relic.
Liudmila Molkova 00:10:18 Right, right, right.
Trask Stalnaker 00:10:21 That's a good idea.
Liudmila Molkova 00:10:24 Allen rare I can ping Alan.
And and then would be per petter be interested in this at all. Do you know Robert.
Robert Pająk 00:10:41 I'm not sure how much his approval will mean. I mean he, we I can ask him. Yeah, I will ask him. Anyway.
it doesn't hurt more approvals is what we need, anyway.
But Piotr is yeah. Piotr is on 3.rd It's he's on leave right now for at least 2 more weeks. So yeah, he won't be able to just realize.
Liudmila Molkova 00:11:17 And I'll ask Colin and Cj. And I think their approval will be will have enough weight for C. Sharp.
Robert Pająk 00:11:25 Okay.
Liudmila Molkova 00:11:28 So what else do we have? C plus plus
Trask Stalnaker 00:11:35 Lollet.
Liudmila Molkova 00:11:39 Can- can you maybe ask him.
Trask Stalnaker 00:11:42 Yeah, yeah. I can ask him.
Liudmila Molkova 00:11:48 I hope I'm spelling his name correctly somebody brought up Erlango at some point.
Austin Parker 00:11:58 I can ping Tristan.
Trask Stalnaker 00:12:03 I thought we had Tristan.
Austin Parker 00:12:05 Have already.
Trask Stalnaker 00:12:06 Already approved it. Oh, yeah.
Austin Parker 00:12:07 Effort.
Liudmila Molkova 00:12:08 Oh!
Austin Parker 00:12:12 My work here is done.
Liudmila Molkova 00:12:15 Nice.
Austin Parker 00:12:25 I have no clue. What I'm backing up right now, Trask.
Trask Stalnaker 00:12:31 This is such a disaster, so.
Austin Parker 00:12:35 And looked. I went and looked. I have like I have been on this fucking slack for years.
Liudmila Molkova 00:12:52 Oh, Javascript!
Robert Pająk 00:12:54 Daniel.
Trask Stalnaker 00:12:58 Didn't.
Liudmila Molkova 00:12:59 Okay.
Trask Stalnaker 00:12:59 Not yet.
Liudmila Molkova 00:13:02 Okay, yeah. And he's been reviewing it actively.
Austin Parker 00:13:06 Over 5 years of DM. History just on this account, not counting my prior account that I don't even know what is anymore.
Trask Stalnaker 00:13:15 That's what I like. I get backing up like I can pick a couple of key channels that I want to back up. But what are we? I don't understand how to do the Dms.
Austin Parker 00:13:27 You have to find the like. DM, id. The channel id for the DM. And then put it in. I.
Trask Stalnaker 00:13:34 For every.
Austin Parker 00:13:36 Is like, Okay, I guess there's 10 people that I that maybe is something important in them. But yeah, this is effed.
Salesforce is on the list.
Liudmila Molkova 00:13:53 Let's move on to teams.
Okay, so it sounds like we have a plan. And we have some open discussions on data. But they are pretty cosmetic, it seems. So far we just need more people to.
Trask Stalnaker 00:14:15 Yeah, correct, I'm gonna try to resolve those like, push little cosmetic changes. Today.
Cause before I I'd like to do that before kind of pinging people, just because when people see a lot of open conversations that can be intimidating to like review.
feel like there's still a lot of open things when they're just cosmetic.
Liudmila Molkova 00:14:51 Okay, yeah. That sounds good.
Trask Stalnaker 00:14:55 So I mean, I can drive all of this today.
Let's just chat.
Let me laugh.
Liudmila Molkova 00:15:07 Okay, do you want to? Yeah, yeah, okay, so were you, you? Resolve existing discussions.
we'll chat, and then we'll coordinate, how when to ping people.
Trask Stalnaker 00:15:23 Ping, people, yeah, yeah.
Liudmila Molkova 00:15:24 Wonderful. Thank you.
Should we reach out to everybody the collector folks? They wouldn't care right. They they already have extended attributes everywhere.
Robert Pająk 00:15:40 Yes, that that's why they should approve as well. Right.
Liudmila Molkova 00:15:44 Oh, okay, Robert, can you ping them?
I think you you have.
Robert Pająk 00:15:50 I can ask. I can ask Pablo from Gc. As well.
Trask Stalnaker 00:16:03 Yeah. I mean, if you wanna just I I can just blast all of these people once we're ready, it's might be easier.
Liudmila Molkova 00:16:15 Okay.
Yeah.
Trask Stalnaker 00:16:29 Bob Bob for? Php, yeah.
Liudmila Molkova 00:16:38 Okay.
Anyway.
Trask Stalnaker 00:16:44 Yeah.
Liudmila Molkova 00:16:46 Thank you. Trust?
Okay.
So we don't have anything else on the agenda. But maybe we can look at our project board. And I was thinking that I kinda wanna understand what we are doing next and how we are implementing those autops that we've managed to get merged or will manage to get merged.
Trask Stalnaker 00:17:19 Before we move on. Maybe do you mind if I share, and we can just look through the discussions on the Otep? Just make sure that we're all aligned on how to resolve these.
This one looks like just resolve it.
This one, I think I agree.
do we? Should I just resolve it? Or do you think there's enough ambiguity here to is there a simple change we can make, or
Liudmila Molkova 00:18:29 I mean, we can change into, or so it formally satisfies.
Let's.
Robert Pająk 00:18:37 That's what they call as well.
Austin Parker 00:18:40 I mean, I don't see that the I don't know.
Yeah, go on.
Trask Stalnaker 00:18:52 Do we need the is, does this mean anything? Do we just want a sorry? The do we just want should provide efficient, deep equality check?
Does that.
Liudmila Molkova 00:19:08 Yeah.
Robert Pająk 00:19:10 It doesn't need to be. The Dp quality doesn't need to be efficient. I don't think it's possible.
Liudmila Molkova 00:19:16 I mean, there are different ways like there are different.
Trask Stalnaker 00:19:20 Nice, which is in.
Liudmila Molkova 00:19:21 Orders of magnitude how inefficient it could be, and you should probably pick the least inefficient one.
But I mean.
the efficient way would be the some sort of a hash code like they are dependent. But we can probably just limit it to deeper quality rate. It's the only thing we actually care about.
Austin Parker 00:19:46 We care about the equality? Right? Yeah.
Liudmila Molkova 00:19:50 Right and just. The hash code is the means to.
Austin Parker 00:19:54 Yeah, I'm just trying to think like, I guess if you in something where you had guaranteed ordering. So if you had like a set implementation.
Liudmila Molkova 00:20:09 You can have ordering, and then your deeper quality comes from the track.
Austin Parker 00:20:17 Yeah, from the order being the same.
Robert Pająk 00:20:20 That's what we have done in the Go prototype.
Liudmila Molkova 00:20:24 But then it's also a means to the end to achieve deeper quality.
Austin Parker 00:20:29 Maybe it's just a clarifying note like.
why like is it? Would it make sense just to be like should provide efficient hash code and deep equality check semicolon. Here's our rationale.
Liudmila Molkova 00:20:45 I wonder if it's already for metrics? Right?
Yeah. Well, resources as well.
Austin Parker 00:20:52 Resources. It's possible.
Trask Stalnaker 00:20:56 Yeah.
Robert Pająk 00:20:59 So.
Austin Parker 00:21:02 You only get.
Robert Pająk 00:21:02 Important to identify. That's where the cash code usually comes in place.
Austin Parker 00:21:06 Yeah.
Liudmila Molkova 00:21:10 So the okay. So the hash code is also yeah. It's just that the 1st thing I stumbled upon in python, because if you have a dictionary of matter, identities of instrument identities and time series identities. Then you kinda.
Austin Parker 00:21:28 May need it to be hashable Python and Java, and I think C. Sharp.
Liudmila Molkova 00:21:38 Yeah. So in C sharp, at least it's you can use something. The map dictionary is a key in dictionary.
Austin Parker 00:21:51 Yeah. Isn't that like a hashable trait, or whatever.
Liudmila Molkova 00:21:54 Yeah, in python. You can't. And unless you do something explicit.
Trask Stalnaker 00:22:02 What do you feel about this just removing efficient hash code and cause? We are already saying that for metric, if you're using any values as metric attributes. It's not gonna be so performant.
Austin Parker 00:22:19 Yeah, I think that's fine. I think.
Liudmila Molkova 00:22:23 Yeah.
Austin Parker 00:22:24 It gives improvement.
Yeah, that's fine. I don't want people like over to too closely, Re, or I feel like half the time I write something in an Otip, and people like read it too closely and half the time not closely enough.
But yeah, focusing on the outcome seems better here.
Liudmila Molkova 00:22:48 Yeah, we'll probably get back to the discussion once we actually do changes in the spec. But in the top the last, we say the better.
Robert Pająk 00:23:02 I still think that adding this or hash code is a safe thing, especially that this auto can also help implementers, and so far.
or just need it is this, or dashboard.
Trask Stalnaker 00:23:15 But that is that correct cause. I mean, hash code doesn't give equality check hash code is just a 1st step in doing equality.
Robert Pająk 00:23:30 Kind of yes. But for instance, when you're using, you know, hash maps, that's the only thing that works right. That's what defines the quality.
Trask Stalnaker 00:23:38 No, it's just the 1st step to it gives you your hash bucket, and then you still have to check equality against the elements.
Robert Pająk 00:23:48 I think it depends on the implementation of the hash map in Java. Yes, and it should be through 4 other languages.
Trask Stalnaker 00:23:57 I mean, that's the point of a.
Robert Pająk 00:23:58 Question.
Trask Stalnaker 00:23:59 Code is a small rep. It's too small. You you're losing information unless you're talking about fully encoding.
Robert Pająk 00:24:07 The whole value.
Liudmila Molkova 00:24:09 Actually, you can.
Trask Stalnaker 00:24:10 A lossy.
Liudmila Molkova 00:24:12 It. It's.
Robert Pająk 00:24:13 Yes, you're right. You're right.
You're right.
Liudmila Molkova 00:24:15 To assume that somebody would implement efficient IP quality without also implementing efficient hash code. But you kind of need both. You can in theory.
Robert Pająk 00:24:23 Yes.
Liudmila Molkova 00:24:24 And very inefficient hash code and efficient IP quality.
But I'm even taking.
Trask Stalnaker 00:24:29 Now I'm proposing to take out the word efficient here.
Austin Parker 00:24:33 I think taking out a fish is fine, like I think we. I think that if that makes people sleep better, cool like we should not over rotate on that at the Otep level.
Liudmila Molkova 00:24:48 Yeah, it seems, we all agree that the the Trusts version and work.
Austin Parker 00:24:54 Yeah.
Trask Stalnaker 00:24:55 Okay, awesome.
I'm going to take this and committed and resolve.
God thank you.
Liudmila Molkova 00:25:35 Thank you.
Trask Stalnaker 00:25:41 Didn't really. I'm a little don't sort of love. This being a laundry list of everything for historic. The historical record.
Robert Pająk 00:25:55 I think a lot of people are concerned about the you know the backend support. I think it's good to have.
Austin Parker 00:26:03 I think it's good to have.
I mean nothing else that says shows that we did our homework.
Trask Stalnaker 00:26:27 Alright, this one.
Yeah. I thought this was a good point, but I didn't. I think there was just a I don't think that diff was, the suggestion was, Oh.
oh, this is actually a can of worms.
Liudmila Molkova 00:26:44 Yes, right?
Trask Stalnaker 00:26:46 Tell me.
Liudmila Molkova 00:26:48 So the value lends limit.
Where I don't think we apply it to the number of elements in a list.
So today, so you can have an endless, I can say Maxent number maxent elements in the list, and we would dumbly truncate the the values in the list.
So we should either change this behavior and also truncate the number of elements in the list, and then it will be applied to bytes. And all right.
Or, yeah.
I think it. It probably would be a good thing to do. The the only thing I'm worried about is backward compatibility, right? Because we don't do it today for standard our race.
But we cannot bites. That's definitely not the problem. Right?
Trask Stalnaker 00:28:06 Yeah, cause there's no support for bytes today. Anyways.
Liudmila Molkova 00:28:11 Right? Okay, this is not controversial. And then string and byte sounds fine, and if anybody brings up array we'll tell them there is support.
Robert Pająk 00:28:23 But only log records. And this is like all already, a problem in the locks signal.
There's like, I mean, it's yep.
Bytes are supported already in in log records.
Trask Stalnaker 00:28:42 Really.
Robert Pająk 00:28:43 Yes, they are.
Trask Stalnaker 00:28:45 I mean I believe you. You know the spec well. But I I know, like in Java.
Robert Pająk 00:28:53 I know. Probably.
Trask Stalnaker 00:28:55 But
Liudmila Molkova 00:29:02 Hey, Dan? The good question.
Robert Pająk 00:29:04 12 Byte.
Yeah, it's here. It should be here or data. Maybe it wasn't data model.
Trask Stalnaker 00:29:10 Data model.
Robert Pająk 00:29:13 If it doesn't find here.
Austin Parker 00:29:18 Yeah. Yeah.
Oh, there are multiple ways to now. I don't know what all this. Now I know. Understand what all the search boxes are on the github.
I usually just go up to the top and use the combo box.
Trask Stalnaker 00:29:34 Any I thought any. This was only for the log body.
Robert Pająk 00:29:45 No attributes as well.
Trask Stalnaker 00:29:48 Oh, yes, but part of the problem we're trying to solve right now, and nobody's implement. Nobody's implemented this right.
Robert Pająk 00:30:00 Russ did, and.
Austin Parker 00:30:01 Oh!
Robert Pająk 00:30:02 I'm good at, and we didn't go.
Trask Stalnaker 00:30:06 But you're not stable because you're waiting for the outcome of this.
Robert Pająk 00:30:10 Yeah, exactly.
Liudmila Molkova 00:30:11 So maybe we can say string bytes and array, and that when SDK stability permits or something.
So if you didn't stabilize it yet. Then you it's a good time to actually apply limits to all of this.
But I would imagine that for Java, if we're end up having one attribute attributes. Type.
then, whatever applied to erase so far would still apply so no limit.
Robert Pająk 00:31:06 Last time.
Trask Stalnaker 00:31:08 We could make that. I mean.
we don't support bytes today, so we could carve that out.
Liudmila Molkova 00:31:14 Right? Okay, so no controversial thing in this suggestion, then, mostly.
Trask Stalnaker 00:31:23 Mostly
Liudmila Molkova 00:31:34 This pack language is kind of weird. It says you must not truncate the value in other cases, which means you can. Actually, you're in the weird spot.
Think it's in common, or the attribute limits.
Robert Pająk 00:32:01 Kind of someone may want intentionally. Put some kind of a blob to the bytes right.
Liudmila Molkova 00:32:07 But it was the the 1st link.
Trask Stalnaker 00:32:14 Oh, sorry that I'm looking at this one.
I just got pinged Austin, that somebody archived one of the channels, one of our channels.
Kind of.
Austin Parker 00:32:42 Which one.
Trask Stalnaker 00:32:43 I know that was a slack bot. Option.
It's an older one. The 2024 contribute fest.
Austin Parker 00:32:52 Oh, okay.
Trask Stalnaker 00:32:54 Not a problem, but I hope that the slack bot archive doesn't.
Austin Parker 00:33:01 Man. IA lot of those I skipped.
I try to just get useful ones.
Yeah, we'll see.
Trask Stalnaker 00:33:16 Sorry, Ledmilla
Liudmila Molkova 00:33:19 No worries. You're in the fighting. The fire, I understand.
Trask Stalnaker 00:33:24 Value length limit.
It's a string if it's an array of string applied to each value separately.
So what we're saying here is, can we say only for complex attributes. We have a new rule that basically, if it's but if it's any.
if it's a map of things.
Liudmila Molkova 00:34:09 If it's
Trask Stalnaker 00:34:12 We apply the new rule.
Liudmila Molkova 00:34:15 Yeah. But what if it's in a if it's byte array right? If it's bytes?
so the the problematic sentence is the 3rd point bullet point. Otherwise the value must not be truncated. Right? So we can in theory keep extending this list and say, Okay, if it's the the bytes, then apply to the number of them are, I, I think, like what I. What I want us to be at is that in the top we kinda agree that we need to figure this out.
Robert Pająk 00:35:02 But yeah, I just want to point out that this bullet point is only for string length limit or not. No, no, I see if it's a string.
Yeah, I see.
Oh.
Liudmila Molkova 00:35:22 So we will need to find a way to change this part of the spec, and hopefully, we agree that the 3rd bullet point well, we can expand the list.
Robert Pająk 00:35:35 Or we can, or we can have a attribute bytes, value left.
Liudmila Molkova 00:35:45 Yeah.
Robert Pająk 00:35:48 Because we have also, yeah, set a limit of unique attribute keys. So this is this, attribute count right?
Not length, but countless.
Liudmila Molkova 00:35:58 Lens. Yeah. So today there is no way to limit the array lens. Maybe the backward, compatible way to get out of this would be in touch to introduce the 3rd option, the attribute.
the array.
Austin Parker 00:36:13 The array, count.
Liudmila Molkova 00:36:14 Can't limit.
Austin Parker 00:36:17 Would that be? That would be recurre, not recursive? That would be.
There'd be a check for the length of the value.
Robert Pająk 00:36:28 Since right now the Otep saying that the Count will be counting the leaf notes, which will be the number of items, etc.
Austin Parker 00:36:37 Well, array is one thing, right?
Yeah, it depends on how you look at it.
Well, wait. Doesn't it? Say I thought it said, that we treat an array as an opaque Any value.
Liudmila Molkova 00:36:54 I don't think we see it.
Austin Parker 00:36:56 I thought I meant in the existing data model.
I agree. This is like confusing, because if I have an array, if I have, I mean, if I have a like, the simplest case is, I have a complex attribute, that is a key.
and then a value, and the value is an array of strings.
Logically, each element of that array is a leaf node of the complex attribute.
Liudmila Molkova 00:37:42 Logically.
Austin Parker 00:37:46 I can't blindly truncate the array value as an opaque blob, because then it's no longer an array.
Liudmila Molkova 00:37:57 What?
Austin Parker 00:37:58 Well, if the array, if it's like, if the array is a string, I can't just like chop off the end of it right? I can't. Blindly. I could remove elements from an array, but I can't like just truncate.
Liudmila Molkova 00:38:19 We are.
Austin Parker 00:38:20 Alrighty!
Liudmila Molkova 00:38:20 Today to turnkey, to trim every element of the array, to the up, to the maximum, up to the limit.
up to the value lens limit.
Austin Parker 00:38:33 Right. So I would need to.
Or yeah. So you would need to be able to set 2 things. You just say, like, array.
length, limit and then value length, limit, and then make sure that no individual element of the array exceeds the value limit.
and also make sure that the array itself doesn't exceed the count limit.
Liudmila Molkova 00:39:00 Yeah, and we can find different ways to solve this problem. And at least, there is one that does it in the back for compatible manners through additional limit. I wonder if we really need to figure it out in the scope of the auto. Sounds like a deep spec discussion.
Austin Parker 00:39:19 Yeah, I guess not.
Trask Stalnaker 00:39:22 I like the idea, though, of that separate
Austin Parker 00:39:29 A separate value. Yeah.
Trask Stalnaker 00:39:30 Basically, here's we've got attribute value length limit. And we've got attribute object length limit.
And then we can say, this new limit gets applied the way that we want to go.
It gets applied to a raise consistently, and any values and everything, whereas this the old one is, has this sort of limiting more limited.
But I agree, how do we? I don't want to introduce something like that at this hour in the Otep.
Liudmila Molkova 00:40:19 Should we just say, Oh, well, how?
Oh, I mean, if we want to introduce it, it's probably worth mentioning mentioning it, that we will introduce another limit for the A race, or we can say, you know what somehow we will figure out how to apply limits.
Austin Parker 00:40:51 Has anyone already done this.
Liudmila Molkova 00:40:56 And prototype.
Austin Parker 00:40:58 Yeah, like in any or any of the specs where or any of the implementations where we've like, partially done this, has anyone.
Liudmila Molkova 00:41:08 I not for the array lens.
but I can update my python prototype, but it's it's pretty straightforward, right.
Austin Parker 00:41:19 Yeah, no, no, no, yeah.
I mean checking the link from an array is at least easy every and fast everywhere. That's that's actually the part that's like less concerning to me.
although I guess, checking the only I think we should just do this.
What Trask is doing.
I like this.
Liudmila Molkova 00:42:12 Is it a replacement, though, like we would still apply attribute limits plus introduce the array limits.
But we we can like shed.
Trask Stalnaker 00:42:25 I don't see this, does. This one doesn't seem to apply to.
I would say this one doesn't apply to complex.
Austin Parker 00:42:41 I agree, I think. Oh, go on.
Liudmila Molkova 00:42:44 What you are saying. It applies to the leaf nodes of complex attributes.
Trask Stalnaker 00:42:52 Individually.
Liudmila Molkova 00:42:54 Individually. So if you have, that's think at least no, Danny.
Austin Parker 00:42:59 No.
Liudmila Molkova 00:42:59 Clyde.
Austin Parker 00:43:00 But the reason I like what Trask wrote is that I also think I think there will be a desire to apply complexity limits to the actual attributes themselves.
Trask Stalnaker 00:43:18 But we could do both.
Austin Parker 00:43:20 Right, I'm saying like you. It doesn't like restricting ourselves to leaf nodes is one thing, but I can definitely see like a a really straightforward example is a limit, a limiter that says this can only be 5 like you. Only this only gets parsed up to 2 layers deep.
Yeah, we can
Liudmila Molkova 00:43:49 Can definitely add one like this as incremental thing right, still need some safe belts, and one of them is no unlimited strings, right? No unlimited erase. That's the one we are currently missing.
and the number of either unique attributes or unique leaf nodes.
And some of the existing limits apply, and we describe how they are going to apply. But we are adding another one for attributes.
and I would imagine it apply. It would apply this in the same way to complex and standard attributes. Specifically because we will not have this distinction anymore.
Trask Stalnaker 00:44:55 So what we're saying is should apply existing.
Attribute limits. And we're saying this, I keep not selecting enough text that I want to change.
Liudmila Molkova 00:45:19 Yeah, I wish it was easier to, you know. Change your mind how much context you want to include.
Trask Stalnaker 00:45:26 Yeah, we're just gonna take this whole section, attribute limits.
Okay?
So we should apply existing attribute limits. Should apply to all leaf string nodes.
Yes, cause that's what the existing one says and what we're wanna say. In addition.
the SDK should.
Liudmila Molkova 00:46:33 Top level.
Trask Stalnaker 00:46:35 Meaning like not.
I guess that's not.
Liudmila Molkova 00:46:38 Of course they're there right.
Trask Stalnaker 00:46:42 Yeah.
Liudmila Molkova 00:46:44 8 9 weeks.
Trask Stalnaker 00:46:46 Yeah, yeah. Ignore me. I was on a sure.
Liudmila Molkova 00:46:51 Did it limit? Do you want it to limit the number of keys in the maps? Because we are limiting them through the attribute, count.
We count them towards video attributes.
Trask Stalnaker 00:47:08 No, I mostly the new that applies so value length, a new value, length.
Liudmila Molkova 00:47:23 They're free to erase and bytes.
I I'm not sure I understand how it applies to complex attributes.
Trask Stalnaker 00:47:47 This would be saying that I have one complex attribute.
And if I sum up the length of all of its size that should be limited.
If I recursively add up all the pieces.
Liudmila Molkova 00:48:14 I I don't follow.
Trask Stalnaker 00:48:19 Yeah, I mean, maybe it's not important.
I mean, if you limit the size of any individual piece and you limit the number of pieces. You've got an effective cap.
Austin Parker 00:48:46 I think.
I think limiting the problem is, you can think about edge cases really easily. For this.
Liudmila Molkova 00:49:15 Oh, wait the length of the string, and bytes leave notes.
Austin Parker 00:49:21 Because you can see, yeah, because you can. You can easily imagine a situation where I could create an array where the combination like either I would need validation or something to stop the combination.
So yeah, like, I don't know. Like, without some some math happening.
you couldn't write a rule that was balance the individual length of a string or byte array in a array.
and also the number of items in the array to make sure that the come that those 2 things combined did not make the array the containing array longer than some value.
Because what do you truncate in that point right like, what is the thing like? What wins you could like if you, a recursive solver for this would be like stupidly complex. I think you see.
Liudmila Molkova 00:50:34 Accumulate. You. Just think about each ray.
and it's 1 thing, a pack thing. You remove elements from it, and then you'll recourse into each individual element in this array.
and do the same.
Austin Parker 00:50:47 Right. But what happens if the company, like what happens is, even after that I my array, is still bigger than some than than the like array, value, size.
Liudmila Molkova 00:51:05 To you, Rick.
Austin Parker 00:51:06 Characters, or invites, or whatever.
Liudmila Molkova 00:51:17 So you walk through the tree.
Austin Parker 00:51:21 If it's if it's a string, you truncate it.
Liudmila Molkova 00:51:25 If it's an array, you truncate it, then you recourse into individual elements, and rinse and repeat.
the moment you discover a leaf node, you count it.
and then, once you reach that, the the cap for the number of unique things say, oh, you're done. You cannot modify this thing. It's too big drop it.
Trask Stalnaker 00:51:58 So the existing rule has doesn't handle erase.
Liudmila Molkova 00:52:08 At all.
Trask Stalnaker 00:52:10 Because unique attribute. The count doesn't factor in the number of arrays. So if you have an array, you have a limit of 10.
You could still have an array of a million elements that each have length 10.
Liudmila Molkova 00:52:31 Yeah. So maybe what we can do. So what I'm suggesting is to add, like, there are 2. There is a nested list here.
and maybe we should have this shared top level bullet point saying, set the limit of attribute of of array or bytes attribute lance.
and maybe maybe you can get away with. Okay, we will. I can try to send a Pr that modifies the existing spec in development. And we can reference this Pr from from the hotel and say, Okay, whatever we end up doing in this pr, the odd tab I don't want Autock to essentially design it.
Austin Parker 00:53:26 Yeah, no, I agree. I just, I'm.
Trask Stalnaker 00:53:30 So can I make get capture what you were suggesting? Let me know. You're suggesting a new attribute limit that would be array length.
Liudmila Molkova 00:53:42 Yeah, that's what they also apply to bytes.
And the SDK will truncate.
Oh, the erase plain or incite complex attributes to this limit.
Trask Stalnaker 00:54:06 Okay?
And so this is essentially needed already it.
If we had this, then if we come back here.
so we would be applying that new attribute limit.
so the length limit would be applied to all leaf string nodes. I won't commit this, but the array length limit to all.
Liudmila Molkova 00:54:58 Every nodes.
Trask Stalnaker 00:54:59 Say nodes.
Liudmila Molkova 00:55:06 Right.
Trask Stalnaker 00:55:14 I wish that bytes feel like bytes should be in the same bucket as strings.
Liudmila Molkova 00:55:26 Yeah.
Austin Parker 00:55:29 I agreed.
Trask Stalnaker 00:55:32 But can we?
Liudmila Molkova 00:55:35 We can commit. What Tigran suggested, and call it a day.
Trask Stalnaker 00:55:45 Yeah, and send a separate try to tackle this problems separately.
Austin Parker 00:55:54 I think that makes the most sense.
Trask Stalnaker 00:55:57 Yeah, at least until somebody asks us to tackle this problem inside.
Yes, yes, okay.
Fantastic.
Liudmila Molkova 00:56:06 Sorry for opening the can of worms, but I I warned you.
Trask Stalnaker 00:56:13 Fair.
Robert Pająk 00:56:14 Is collector doing any attributes, limitation, or things like that.
Liudmila Molkova 00:56:20 I don't know.
Austin Parker 00:56:21 I mean, there's some ottl stuff.
Robert Pająk 00:56:28 That means something by default, like or year, or are just this limits only for the sdks and not for the collector.
Austin Parker 00:56:41 That I don't know.
Trask Stalnaker 00:56:42 These limits are for the SDK, I mean in the spec. At least, right? I mean it. I think it's SDK now the collector uses an s the go SDK so.
Robert Pająk 00:56:55 Like, for instance, the attributes and limits are defined in the common attributes. It's not SDK something global.
If I remember correctly.
Trask Stalnaker 00:57:10 Sorry I didn't follow.
Robert Pająk 00:57:12 I. I want to say that the attributes for the limits for attributes, I think, are defined in the common in the command for Directory. I don't think they're they are defined in the SDK.
I think their environmental variables in the configuration and SDK configuration by, etc. But I think the limit themselves are defined in in some common, you know. Data model ish thing, not in the SDK.
Trask Stalnaker 00:57:43 So are you. Saying, therefore, it applies to the collector.
Robert Pająk 00:57:47 Yes, that's that's what I understand.
Trask Stalnaker 00:57:52 Don't think the collector folks think that be any part of the spec like applies to them, but I guess that's.
Robert Pająk 00:58:03 Yeah. So what's the reason to have limits on this? The case, and not have on the collector, etcetera.
Austin Parker 00:58:10 Because the collector is unspecified.
Liudmila Molkova 00:58:14 Also because.
Trask Stalnaker 00:58:15 I don't think it's the current practice.
I'm not saying it's a bad idea.
Liudmila Molkova 00:58:23 It, it would apply only to instrumentations right to some receivers.
If if you're a collector and you received unbound value a huge attribute. Why would you drop it? Somebody managed to export it. That was users desire to export it.
Robert Pająk 00:58:45 Yeah, but same could be said on the, you know, education.
Liudmila Molkova 00:58:49 On the SDK. I think the reasoning behind it is that as not.
no, it's that it has to be a. It has to consume a limited amount of resources because it's in the process, and it affects your process. Perform performance directly. So if somebody pushes 1 GB attribute into your span. Then the SDK will keep it in the memory until it's exported, and probably never.
Robert Pająk 00:59:20 But same applies for the collector, receivers.
Trask Stalnaker 00:59:22 I think we are way off. Topic here. I.
Robert Pająk 00:59:25 Yeah. Yep, no, my, my my question was because I think they may be some limits there applied. Maybe they already are doing something. Maybe they already have some configuration. It was more about asking for prior art than asking them to do the same.
Trask Stalnaker 00:59:43 Okay.
alright. I'll go through the rest of those comments. And let me, I'll sync with you later today on messaging.
Liudmila Molkova 00:59:59 Thank you.
Trask Stalnaker 01:00:01 Thanks. Tom.
Robert Pająk 01:00:02 Bye.
Liudmila Molkova 01:00:03 Here.
Austin Parker 01:00:03 Hi! Everyone.
