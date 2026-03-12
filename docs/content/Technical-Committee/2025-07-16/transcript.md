SIG: Technical Committee
Date: 2025-07-16
Duration: 43 minutes
============================================================

## Zoom Recording Transcript

**Liudmila Molkova** 00:39 Hello! Good morning!
**Josh Suereth** 00:46 Morning. How's it going.
**Liudmila Molkova** 00:50 Haven't seen you in a while, Josh.
**Josh Suereth** 00:56 Yeah, I do think I need to get some meetings sorted to make sure.
I think time and length and duration of meetings are a little off for some of my open telemetry meetings, so I need to get that sorted. There's a bunch that go long.
and there's a bunch that are just not useful discussions that go that fill the time.
And so.
anyway, I was just thinking about how we end up running out of time all the time before the Tc. Meeting.
Maybe we should move that some somewhere else where we can run over. Yeah.
So I saw Carlos is going to be late. Do we know? Is Armen out, too?
Can you hear me?
Okay.
I think according to the rotation, it says, Riley, is the current runner of this meeting.
**Liudmila Molkova** 03:31 I was looking for it. Where did you find it?
**Reiley Yang** 03:36 But no, I saw a rotation, Doc, where we see the spec meeting and the security.
I don't even know we have a rotation for Tc. Meeting.
**Josh Suereth** 03:47 We do. It's it's linked from the Tc. Notes, Doc. As well. So at the top there's duty rotations. And here I'll present because actually, one of my topics is the this rotation document.
**Reiley Yang** 04:04 And I'm probably missing.
**Josh Suereth** 04:05 I could make a spreadsheet that automates it. So over here is the communication rotation on the right which run the Tc meeting. Take notes and Tc. Meeting, and it is the week of the 17.th So that would be Riley. Jack, you know, as you know, is on leave, and so I know he set this up last week and ran the meeting last week. But yeah, and then I'm I'm the week after. So anyway, are you able to run the meeting. Riley.
**Reiley Yang** 04:32 I can, I'll I'll put a doc. And I guess this was probably discussed previously, which I didn't join, and I look at this like my. My concern is this, rotation makes you almost like busy every week. So have we discussed that we want to align this. So so you have a busy week. You just take care of all of them.
**Josh Suereth** 04:56 That's a possibility. Let's let's talk about that. I want to show do you want to talk about that? Now I have. If you look at the agenda.
**Reiley Yang** 05:03 You can follow the agenda.
**Josh Suereth** 05:05 Yeah, I added a bunch. I did a bunch of talks, the security rotation one. If Armin's here now. So I think we can talk about that.
Then, automating the rotations, I tried to make a more automation with a spreadsheet. We can decide if that's enough. But I just spent like 10 min with Gemini making some crap, and you can see what I did, and tell me if you like it. But if we wanted to do what you're suggesting. I think we have some possibilities. There.
**Reiley Yang** 05:35 Yeah, you can. You can stop sharing. I'll share.
**Josh Suereth** 05:37 You got it. Okay.
**Reiley Yang** 05:47 Sorry.
Give me a second.
You see my screen.
**Armin (Dynatrace)** 06:05 Yep.
**Reiley Yang** 06:06 Okay, then, Josh, you go first.st I'll I'll add my topic later.
**Josh Suereth** 06:11 Yeah. So this is I don't. I don't know if we're I. By the way, apologies, I have to leave about 15 min before the end of this meeting to go pick up my daughter. So need to rush some topics. But the security rotation basically the dashboard that we use to track long running bugs is broken. So we've been using the Github audit logs for when security vulnerabilities are reported to check on recent things, but in terms of tracking status until that dashboard is fixed. It's kind of awkward, too.
Just wanted to see like I know, Armin, you had raised this before. Who do we think should own this? Is this something we should give to the security significance? Is this something we should talk to the Gc about?
that's part one of the question. And then part 2 is, we actually have to pass credentials around each other, since we no longer have admin control of the Github org. That's not part of the Admin Sig and the Admin team. If you want to see these, the if you want to see these things, you actually need to have admin credentials to Github again. For now we're planning to just basically whoever was on security rotation that week. The next week they give the credential to the next person and take themselves away unless they're on the admin rotation, in which case they will have the credentials. Still, those are. Those are kind of my 2 concerns. Here is like, Are we?
Are we okay with that? Who? Yeah. So I'll just write this? Who owns fixing the security dashboard.
Do you see?
CC.
Security, Sig.
**Reiley Yang** 08:00 For that. Do we really need the dashboard or not?
**Josh Suereth** 08:20 I I don't know, Armin. I don't know if you want to speak, speak to this, but when I reading the dashboard I thought it was pretty handy.
**Armin (Dynatrace)** 08:28 I, I think the same. It's pretty helpful. The audit log is good enough, if you're on duty and you bookmark the open one, and you keep checking the bookmark. It. It works as well. You just have to have an idea of what's still open, or you just open the last few ones in the in the audit log. Because if it's less than a month old, chances are it's still open, but it's still more error prone and not as nice as the dashboard. I think the dashboard still makes sense.
and also we could, for example, give access to the Gc. To that dashboard, for example. So I think it makes sense. If it would be super cumbersome to fix or or have some other disadvantages, we might reconsider it, but I could imagine once we find out where that workflow lives. I don't know if it's a sapi automation, or whatever to be honest. But it might just be a token that we have to update.
and then we should be good again.
**Reiley Yang** 09:34 Yeah, some big memory. It's it's probably created as a branch in the 6 Security Repository. And there's some Ci job that runs every day.
and I've never used the dashboard and so hard for me to comment. But I I was able to handle security issues and work with the Maintainers before without the dashboard, and I'm curious about when you look at the dashboard.
What actions are you going to take? And are you going to look at the dashboard every day. So maybe, like I have a different behavior. So I I barely look at the dashboard because, like I, I feel like checking that every day, or something is just like very tedious. And I I tend to automate this, and by automatically assigning things to people like through automation. So I'm I'm curious when you look at the dashboard. What are the things you're going to follow up.
**Armin (Dynatrace)** 10:31 I would follow up all open items. Usually it's not that many, and nothing should be open deliberately. So what I would do is, I look at all of them, and if I've just passed many maintainers the previous day to look into it, then I will probably hold off. Hold off for today, but then the next day I will bug them again about it, so I would.
**Reiley Yang** 10:59 I see.
**Armin (Dynatrace)** 10:59 At least like, think about all open items once, even if there's no action required at this point.
**Josh Suereth** 11:07 I think so. The the date that it would list of how long it's been open and ordering it by longest open is super useful right?
Because because it gives you a prioritized list of like, okay, look at the one that's been open the longest and make sure the status is okay? And you can do that every day. See if it's making progress reach out to maintainers if they need help. That kind of thing. So yeah, I absolutely agree with Armin.
**Reiley Yang** 11:30 I see. Thanks.
**Liudmila Molkova** 11:38 Do we have a dog that describes what to do.
**Josh Suereth** 11:46 I think no, and I think the person who made the from from what I understand, Armen, correct me if I'm wrong from your comment. The person who made the dashboard in the security sake is no longer active in the security sake.
So I think the question here is like we should find an owner for this dashboard. Is it still the security sake? If so, can we get the Security sick to fix it for us?
Or is it something that we should take ownership of and own as the Tc.
And you know, figure that out so that our on call has it? Or is it something we want to ask the Gc. To take ownership of, like, I think those are kind of the 3 places that I think it could belong. Riley, you speak on behalf of security sake. Is this something the Security sick should own and and update and maintain.
**Reiley Yang** 12:29 I can't share my personal opinion, so I like I I don't feel the Security State should own it.
Currently, the security sake is more about providing guidance and find out the overall security prioritization, handling, security. Vulnerability is already a very clear thing. So we're part of like executing towards that. Who's going to fix the issue is not something security seek is focusing on.
**Armin (Dynatrace)** 12:58 I I think the question is twofold like, who owns the the tooling that that feeds the dashboard, and who owns the dashboard? That might be something that that security seek could could keep. Or yeah, I think they have it already, so keep it. But then, being responsible for getting the vulnerabilities closed and and addressed. That's something that could lie well within Tc, or gc, that's also the the topic, because you need access to the to like the the full security advisory, content and such. I think that's where we wanted to have a high bar of who gets advanced knowledge about it.
And that's why I think we said that we have it within the Tc. And or Gc, only right?
But for the tooling itself.
that that's something that could be within a Sig.
**Reiley Yang** 13:58 Yeah, currently, it's not security sake, like the the repo is more focusing on like docs and process procedures. And what like, what's the guidance for Maintainers, and and I guess this is also why the dashboard was never officially documented. It's what it was never checked into the main branch. It's just a separate branch, more like a personal product. We we were trying to get feedback before we figure out how to make it more formal.
**Josh Suereth** 14:39 So from. I'll just. I think we'd like this dashboard, because I think it provided a default view of all active vulnerabilities and the priority, we should look at them right? Just like how long they've been open. And from that standpoint I I personally think, like the Sig Sig security, basically creating the dashboard that says, Here, here's the things we need to look at, and the most important security vulnerabilities for us to address. So whoever's on call just focuses on that. So the the thing where you said 6 security provides recommendations about what to do. Who owns the tooling for the dashboard, I think, would be 6 security to say, Here's, Hey, here's what you need to focus on. And we can give this. We can make sure we use this on our rotation. Then, to make sure we're driving towards the most important things to do. So like that. That's kind of my perspective here. But if the Security sick doesn't want to fix and maintain the dashboard. We'll we'll continue to you. We need to do something, so we'll just continue to to look at audit logs, for now we'll continue to pass credentials. But I don't wanna take too much more time on this. I, Riley, if if like, let us know your your opinion, but I might open a bug against the sick security about the dashboard, not working to to fix it right? Okay? And like what what we'd like to see from it for our rotation.
**Reiley Yang** 16:03 Yeah, just to share 1 1 last thing. So think about this from security perspective. We want people to take care of the repository security vulnerabilities. We also want them to take care of the the Ci CD job making sure they're not using an outdated version. And we also want to make sure the Maintainers they have the right access. We don't want people to have admin access to everything right. And we also want people to follow certain guidance. For example, they're not supposed to use an ancient version of Tls. So each of this, I I don't think Security seek currently has the bandwidth to build dashboard for every one of them.
And in my mind it's more like either we have more members joining security sake. So we have domain specific thing similar to how we run semantic convention or the security is going to delegate this work to different teams and maybe security vulnerabilities are handled by the Tc. Then what about the Ci CD job? If people use an ancient version of Ci CD. Job, it won't be reported as a Cbe.
What if the Maintainers don't just like take care of that. They don't have any dependent about or renovate, and they don't update that.
What does that mean? So so in my mind, it's more like a delegation. Maybe we need another rotation just to make sure people don't use a deprecated version of a Ci job and building dashboard for everything like like each dashboard for everything. I just don't think anyone can have the time to go through that like every morning. Imagine you go to 3 like you go through like 20 dashboards, simply not going to work. So we probably need to grow the habit of maintainers taking care of the Cve and have certain mechanism to to raise the priority, so they they don't need someone else to stare at a dashboard and ping them.
**Liudmila Molkova** 18:02 It sounds like we have a process in the Tc. And we need just one dashboard for now. And we need to make sure the process works sounds like we either we want to change the process and then it's the Maintainer job to to look at the dashboards. But we are responsible for the security.
So then, it's our responsibility to know and notify maintainers and make sure they are on it.
and.
**Reiley Yang** 18:33 Yeah.
**Liudmila Molkova** 18:33 Yeah. So this is just one dashboard. We're not talking about 20.
**Reiley Yang** 18:37 So for yeah, I'm giving you the context from security sake. Why, I have a different perspective.
Because Cve is just one part of it. It's an important part, but there are many other parts.
and owning 20 dashboards from the 6. Security is not the goal. In my opinion.
this is context from a different perspective.
**Josh Suereth** 18:59 Yeah, okay, so it sounds like, we need a a broader discussion.
For the purpose for people who are going on the security rotation.
for now we're going to look at audit logs, and I think after me, next is bogged in so. And then you, Riley, so like, for now you're gonna have to do the the process of checking audit logs because I hear what you're saying. But additionally, like someone is ultimately responsible to make sure vulnerabilities in in open telemetry are resolved. And yes, we're deferring to maintainers. But the reason we're checking the reason we're looking at dashboards. The reason we want, like long open cves is to make sure this is finishing right? And yeah, you don't want to breathe down the Maintainer's neck. But we still need to make sure, hold them accountable to finish cves. So we need something. That dashboard was the thing that did that for us. If that is dead and gone. We want something else that does that for us. Who will build that? Who owns it is an open question. I'll open a bug for 6 security if 6 security doesn't want to provide that dashboard for that specific use case.
we can sort it out later. But I think I got the answer to my question here. Nobody really owns the dashboard. It's kind of a No Man's Land should not rely on it, for now that means I'll I'll update some of the description for security rotation to basically say, Hey.
go, read all these things, go look at old ones, and make sure they're getting completed.
And then, when when everyone's on on call, and they have to do this themselves. Eventually someone will be so grumpy about how annoying it is. They'll make a dashboard.
That's that's probably what will happen.
**Reiley Yang** 20:44 Yeah.
**Josh Suereth** 20:45 Bogdan. I don't know if that'll be you, since you're next, but just word of warning. It's exciting.
Alright cool.
Let's see.
**Bogdan Drutu** 20:55 May ping you to help me a bit with that, but agree.
**Liudmila Molkova** 20:59 Can you document the protest place? I posted some random stuff in the chat. I have no idea how credible it is.
**Josh Suereth** 21:07 Okay.
we, we can do that. And I think Armen is the source of truth. For how to best do this because he's been.
are person watching these things for for the most or for the longest. So so, Armin, I will do what I can from what you've explained to me, and what Carlos told me from what you explained to him.
**Armin (Dynatrace)** 21:27 I actually wrote it down somewhere in our slack in a in a thread. But I'll I'll try find that one and send you a link, because apparently it somehow fell under the table right?
**Liudmila Molkova** 21:43 Oh, so sorry I did notice it. It's my my bad.
**Armin (Dynatrace)** 21:47 It's all right.
**Josh Suereth** 21:48 Yeah, I might take it from slack, and anything that I can put publicly in the document I'll try to put in is that fair.
**Armin (Dynatrace)** 21:56 Sounds, good.
**Josh Suereth** 21:58 Mostly because I need to use that every day this week. So I've been doing that alright. Let's move on automating the rotations. So this I I made a spreadsheet. I can give everyone edit access. I didn't have time to do that before the meeting apologies, but if you want to pop this open. This is the same.
the same content as the duty rotation sheet. And I just want to talk through what I did to make the rotations easier to understand. So 1st of all.
the opening of the sheet is just current rotations. It has your. It has the responsibilities. If we want to put a playbook for what you do. We could do that here. So for security rotation, we could call out like the links to things like what Armin has in slack of like the links. You click on what you need to do. That sort of stuff we can put in here. Current assignee is dynamic. It will update every week to the assignee for that week. Right now, the rotations roll over on Monday.
and so that's just currently what's what's going on. Request donation is one we have to update manually because it's on demand. And I'll get into that in a second. There are 4 sheets at the bottom if you click on weekly rotations. This is where we go to transfer. Who owns weeks. Do you mind clicking on weekly rotations, Riley.
So the way this works is, I have all of the weekly assignments here.
and right now it's it's a different person.
And then the dates. This is the same thing that Jack has in his word document, but in a spreadsheet, if you wanted to make new rows, what you would do is you would click on the last date on the left.
and then there's a dropdown on the right that you can drag below. So actually, Bradley, do you mind if I present, maybe I'll maybe that'll make this easier.
Okay, cool.
So on weekly rotations. Yeah, you can click here. And there's I don't know if you can see this, there's this dropdown. If you drag it down, it just keeps adding weeks.
Okay.
and then if you want to make a new rotation. You just grab the Rng from here, copy, paste it, and it does 2 weeks at a time. There are only 9 of us.
So the. And since there's 3 no, there's 8 of us, I guess, in this, since since we can only do so many rotations, it was like one short because of how many Tc members there are. But what you can do is if you just click anywhere and you press delete.
it'll reroll the random Rng for for what? Tc members. It selects. Okay.
any change to the spreadsheet changes the Rng, but the idea is, we take this, we control c, we control. V, and oh, man.
okay, maybe we had.
This was.
**Reiley Yang** 25:01 I have a question. So so why do we need this to be such complex? Can we have like like, you're the primary, and you just handle everything this week.
**Josh Suereth** 25:11 We? We can do that. That is not how the rotations were set up by Jack.
**Reiley Yang** 25:15 Okay.
**Josh Suereth** 25:16 In the last minute. I wasn't in the meeting where we agreed to the rotations. I I agreed to the rotations I was in the meeting where we agreed, so I don't know why they're all split up. That is a thing we can discuss, and I think we could change that. And this could be changed where it's like, okay, the next week would be Carlos. Then, after that is Riley. Then after that is Armand. After this, Jack, the way this works here is. It's just creating a random array for people and flinging them out randomly. So every time you hit Delete, it just puts us in a random order, that's all it's doing. And it's grabbing from this list of people right?
In any case, what I was trying to do. I have a few goals? One is, I want to make it easy for you to know when you're responsible for something. So you, if you need to go on vacation. You look at your week.
you update it in the existing rotation calendar. Right? It's a little bit more awkward because the current upcoming rotations are all at the bottom, and we have to manually update the assignee.
So I'm just doing minor improvements to make this easier for us. So if I know I'm going on vacation in the new sheet. I can go and say cool. I need to go on vacation this week. Crap! I'm on call. Let me ask someone before or after to switch with me.
Right?
That's that's it. So that's what I wanted to do. I added this randomized thing so that we can actually fill out the rotation faster in the future and then on demand rotations. It's just keeping track of who signed up for what we can do things like calculate, who has taken on the most requests and figure out load. And but this is just keeping track of what we've done. So we can kind of keep things fair.
Okay, that's the proposal here is is I'd I'd like to move from the word document to the sheet. I think it's an improvement, with no loss of information.
but wanted to run it by everybody.
Unfortunately, Jack's not here. Who made the the 1st sheet.
**Reiley Yang** 27:20 Yeah, I don't have a strong opinion to the tool. I think either a word document, or a spreadsheet would be fine. I do have feedback and concern about the complexity of this. My suggestion is just make it simple.
like you're the primary for this entire week, and after that you're done. Instead of you have 4 different things. I probably have a smaller screen. So when I look at the word document, I look at the 1st 3 columns yesterday, and then I noticed, like Josh, you were supposed to run the spec meeting, and it turned out to be Carlos. So I wonder maybe this is a ongoing discussion. Never.
**Josh Suereth** 27:52 I'm the security. I'm the Security Lead. Carlos was the spec lead this week. Last week I ran a spec meeting. Yes.
**Reiley Yang** 27:59 I see.
And I got confused about this. So let me just make make it simple. You have one rotation instead of 4, because we? I imagine we'll we'll we'll maybe add another thing, and the the columns will keep increasing.
**Josh Suereth** 28:17 I think the idea behind separate rotations and separate people is not to overload any one individual person with too much responsibility.
I think that was the idea before I given given how much the security rotation has taken out of me. Given how much the specification leading was, I think it's reasonable that we could have the same person for all 3 if if we wanted to, as a group. But I'm kind of curious other folks who, you know who have already been on a rotation. How do you feel, you know, like.
do would you want to do all 3 at the same time, and then have a longer delay before you have to do more things.
**Carlos Alberto Cortez** 28:57 I guess that one question that I have is how many hours or how much time you think this would take from your actual day job, you know.
if it's not a burden, I think that would be better, because the 5.
**Reiley Yang** 29:15 I mean, it's taking, and some additional communication in total. I wouldn't expect more than 1 h per week.
Then running the Tc.
It's off, probably like 4 or 5 h per week.
**Liudmila Molkova** 29:39 My main concern is, if we have multiple rotations you participate in, it's that we will forget. I will forget. It's hard to discover that they should be on the specification leading, the specification being, I might discover it 5 min into the call. It sucks.
So if it's 1 person for everything.
It's probably manageable from time perspective, at least the subjective feeling cause that. But it's easier to discover that you are on call for the whole week or open telemetry. Well, on all quotes.
**Josh Suereth** 30:17 I I hear you.
Yeah.
take vacation and ask for people to take a rotation.
I'm fine with, what what do we think about for now, since since again, Jack's not here, and I want to be sensitive to that, if we wanted to have the same person on all the rotations, and we all agreed to it. We should do a vote.
we. I can just update the weekly rotations to have the same person for all 3 going forward.
And we can. When we expand the sheet, we can just have the same person for all 3. And then we know that for now all these rotations and responsibilities will say the same person for a particular week.
We have a sheet that tells you the up to date person who's responsible, and if we want to split in the future, we can right.
**Liudmila Molkova** 31:29 And we can try.
**Josh Suereth** 31:31 Yeah, go for it.
**Reiley Yang** 31:33 So if we have like, if we have a like a a dedicated person for the week for everything, then we don't need to have all these columns right like we can make it simpler, and we probably don't even need this spreadsheet. We can just publish that on the on the open telemetry calendar. So we communicate to people. The Tc like one Tc. Member, will be accountable for this type of things for this week. If you have specific thing you need to reach out to Tc, here's the public information, and it's on the calendar. It's very easy to check. You don't have a separate doc or spreadsheet.
**Josh Suereth** 32:10 Yeah. The the only annoying thing about calendar is may like changing what it is when you go on vacation and swapping with someone is a pain in the ass, a spreadsheet. It's a copy paste I'm trying to optimize for what I think are the key things we will need, which is who is on call.
and can I take vacation? Those are the 2 most important use cases I found for any kind of on-call rotation.
If, if calendar made this easy. I'd be all on calendar. But I, freaking hate trying to modify meetings with people right? It's a pain in the butt. If you have that calendar entry automated from something else. Cool? I actually think. And I haven't had a chance to do this.
If I get this into the appropriate Google, you know, ownership from the Gc. We might even be able to use extensions and scripts to just fire calendar note like fire calendar things in the open calendar. So there'll be a thing that says, here's who's on. Call right now because we'll have the app script run every night and synthesize it. That's that's some of the crap we can do here if we want I'm trying to do the minimum first.st So I took what Jack had and just added automation around vacation swaps. And who's on call now? That's all it does it it it also, instead of having to manually randomize people, you just click here. Sorry you click here you hit Delete a few times, bam, you have a random order, you can. You can flush out more more weeks. That that's all this does. It's not meant to be like if we have concerns about who's on and all that cool. Let's have those discussions.
If this is more about just automating what was produced today. And again, don't consider this the final solution. This is just we're we're making progress towards it. Okay.
**Liudmila Molkova** 33:59 I love the spreadsheet. It's just if we have the same person starting. I don't know. Would you be willing to be the next week to try. Do it all in the same time, and if.
**Bogdan Drutu** 34:14 I will try. I will try. Let's see if I succeed or not, but I will try.
**Liudmila Molkova** 34:19 See, I've got from my specification rotation this way.
**Josh Suereth** 34:23 Good good work. Does anyone, does anyone veto that I just want to check first? st We'll just check if there's any dissent, because I'm gonna assume that we're all in agreement. But does anyone disagree, feel free to throw up a reaction like a I don't know Crying face or something? Do we have a reaction that works with thumbs up. That's not a descent. That's a thumbs up. Okay, cool.
**Carlos Alberto Cortez** 34:46 Just confirming, you know.
**Josh Suereth** 34:48 Yeah.
**Armin (Dynatrace)** 34:49 Yes, you object.
**Josh Suereth** 34:54 Alright cool. So what I'm gonna do then is I'm gonna give everyone here edit access. Later, I'll put a note to this in the Tc. Notes. Of right now it'll be here. This is what I'll do, and I can't spell today. Spreadsheet I'll put. I'll put a link here, so you can see this and toy around with it. I'll give everyone edit access. Once everyone has edit access, I'll swap out the duty rotations link for the spreadsheet. So we can start using the spreadsheet, and then we can update the names so that Bogdan gets next week. Thank you, Bogdan, and we'll I'll make a random order for everyone else, understanding that I think Jack is still on leave, so we'll make sure he doesn't fall in that list until we expect him to come back.
**Bogdan Drutu** 35:46 Okay.
Wonderful 1. 1 quick thing for the duties I don't think we do. Weekly releases correct.
Is that something that we wanna I know. I don't know how it will be, but if we go with a week, everyone in we may end up having the same people or the same group of people doing the releases smaller than than everyone.
**Josh Suereth** 36:14 Yes.
**Bogdan Drutu** 36:16 If we do that every 4 weeks, for example.
we are 8. Only 2 people will do all the releases. So.
**Josh Suereth** 36:24 Well, that's that's if we we're not probably not gonna have time to talk about the private topic. But I do think we're not going to be a so that will alleviate some of that. But yeah, I agree with that concern.
I debated going crazy with this Bogdan, and kind of pulling in. If you're familiar with Google's on call tools, figuring out a way to have it like an open source version of that. And I was like. No, let's just keep it dead simple. But there is a way we could like Wait, who is who is there and have it figure out weights. And so the end of the month rotation is weighted higher. And we we make sure that it's distributed across people better. There's like things that we can do. Yeah, random jitter. Yeah, there's things we can do here if we want to get complicated. But I think for now my thinking is, if we know, like end of the month is released, we can actually make account for how many times a person has been scheduled for end of the month weekly rotations.
and we can use that to say, Oh, cool! This person has been end of the month too much. We'll manually change it for now, so we'll just keep track of who? Who's doing the work and and try to balance it that way.
Does that sound good again? Let's start small before we engineer the crap out of it.
**Carlos Alberto Cortez** 37:43 Yeah, I think that it's a great idea. Let's just try something that seems simple enough, that will work. And we can learn from that, and iterate on that.
**Josh Suereth** 37:50 Yeah.
okay, I want to give a quick update. I have to leave in 5 min. So apologies. From the entity Sig. Just we we had the Otep. We started doing prototypes. We had a specification for the SDK. And the the resounding reviews of the SDK. Was this should actually be an Api and I think this is a significant change to what we originally the entities was going to have phase one and phase 2 and phase one was going to be focused on just resource. SDK things the resource SDK things we think we want an Api for, and there's a lot of things to untangle, and I wanted to give you 1st is the prep of Hey, we're having those discussions in entity, Sig. Those discussions will come to specification, Sig, and I want us to get our story straight for how we think about this, but the the general premise is exposing a component of some sort where you can register Api or register resources via an Api semantic conventions for around resource related things would would create instrumentation right? The same way. We have metrics, semantic conventions, span semantic conventions. We'd have resource ones or entity ones.
We have components that people can provide that will do resource detection.
We need to find a way to have those components get registered at the startup of open telemetry sdks so that they happen before the SDK is instantiated.
That's the the next tricky thing. We're trying to figure out what that looks like and what that is. Right now, implicitly, we have this in our specification. Right? Resource, detection exists. It's an SDK only feature. We've given the implementation of it up to all.
all sdks extensibility somewhat awkward right. This is a proposal to kind of formalize it and figure out what that looks like. I think it's rather aggressive. And I think we need folks on the Tc helping sponsor. This we currently. You know, Tigran and I are in entities. Tigran has taken a step back, and I think he's on vacation now. But we're guiding it. I'm actually saying, I think the investment from Tc. Will will need to increase for this sake.
So I'm calling that out now as an escalation, let's talk about what that means, and talk about what it is. But I wanted to give you at least a week to kind of understand this change, think through it, and come and formulate your opinions. I do need to drop in 4 min, so I wasn't ready for a full discussion. This is more a hey? I want to have a discussion.
and I want you all to have time to think. Go ahead, Bogdan. I think you unmuted.
**Bogdan Drutu** 40:43 No, I was not unmuted, and I didn't want to say anything just approving you. What you said.
**Josh Suereth** 40:50 Okay, cool. Yeah. If anyone has major concerns or major vetoes, please let us know right now. Otherwise we're we're the plan is to continue to prototype in the entity Sig and take Ted Young's Otep around entity provider and update that to account for all the things that we need, and then this would come as a 1st and Otep, and then as specification changes. So the specification change you saw for me will remain in draft indefinitely until the Otep plans.
**Bogdan Drutu** 41:20 Okay.
**Josh Suereth** 41:21 Cool the last thing I wanted to talk about, and I have to. I have to drop so apologies. There was a private topic we had from. I think we've been talking about it like last week, a few weeks ago. I think we should continue that discussion.
I will not be able to participate in that discussion today. But I if if you all want to have that discussion without me, please do. I think we need to continue to make progress on that.
**Bogdan Drutu** 41:50 I agree, but I would like you to be there, and probably Pig Run and others so.
**Josh Suereth** 41:57 Yeah, let's let's defer that. Then, to a week where we have at least maybe 8 8 of the 9 of us in the or 7 of the 8 of us. How many of us are there left.
**Carlos Alberto Cortez** 42:08 8, 3.
**Josh Suereth** 42:09 Okay, let's make sure we have at least 7 of the 8 for that discussion.
because I think Jack will be on leave for a good bit.
**Bogdan Drutu** 42:16 Yeah. And without you would be 5. So would be very, very close to half plus one. I would prefer at least 60% to be there. So.
**Josh Suereth** 42:26 Okay.
**Reiley Yang** 42:27 Is there a way to check that like like? Is there a way to check the calendar and see if we can make the call or like, maybe we won't be able to make the call in the next 3 months. Do we? Do we know how to check that.
**Josh Suereth** 42:40 Oh, you mean for vacations.
**Reiley Yang** 42:43 Right.
**Josh Suereth** 42:44 I don't know if if folks are using the hotel vacation calendar or not. I have a hard stop right now, so I do have to leave. Thanks for the discussion on all those topics. I had really appreciate it. And yeah, I'll see you all next week.
**Bogdan Drutu** 43:01 Right.
**Armin (Dynatrace)** 43:02 See you bye.
**Reiley Yang** 43:06 Okay, son, any other topic, or we're done.
**Bogdan Drutu** 43:10 Yeah, correct.
**Reiley Yang** 43:13 Thank you. Bye.
**Carlos Alberto Cortez** 43:14 See you.
**Armin (Dynatrace)** 43:14 Yeah, bye.
