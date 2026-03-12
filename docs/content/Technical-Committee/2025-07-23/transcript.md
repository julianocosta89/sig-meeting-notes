SIG: Technical Committee
Date: 2025-07-23
Duration: 34 minutes
============================================================

## Zoom Recording Transcript

**Tigran Najaryan** 00:14 Hey, Riley.
**Reiley Yang** 00:17 Hey, Taylor.
**Josh Suereth** 00:54 Hey!
**Tigran Najaryan** 01:00 Hey, Josh.
**Josh Suereth** 01:06 How's everybody doing?
**Reiley Yang** 01:10 Good, hearty.
**Tigran Najaryan** 01:11 On you.
**Josh Suereth** 01:13 Pretty good. I feel like it's been the busiest year I've ever had.
Tiger. I was supposed to vacation up your way, but we we were too late to we were gonna take a tour group thing up through. It was like Toronto all the way through Montreal.
And we? We didn't make it. We got on a wait listed, and then, and it didn't come through. So I'm kind of bummed.
**Tigran Najaryan** 01:40 Oh, like you using cars, or what was it?
**Josh Suereth** 01:46 It was gonna be like a big comfy coach bus that would like take you and drive you to a bunch of stuff like all the way. So you get to spend time in Toronto, and then spend time in Montreal, and then head home.
**Tigran Najaryan** 01:56 Yeah, but.
**Josh Suereth** 01:57 Then then to go through like the Canadian wilderness between. There it was a big like.
and then they had. What do you call them 1st 1st nations. There was a bunch of like 1st nation stuff you were gonna do like a cuisine.
It looked cool.
**Tigran Najaryan** 02:11 Yeah, yeah.
**Josh Suereth** 02:12 Yeah, we're gonna try it again. I think maybe next year or the year after, we'll see.
**Tigran Najaryan** 02:18 Yeah, okay.
**Josh Suereth** 02:34 Do we know if if anyone else is coming.
**Tigran Najaryan** 02:42 Are people out this week.
**Josh Suereth** 02:46 I know Ludmilla's out on vacation, and I know it's just generally vacation time.
**Tigran Najaryan** 02:53 Okay, off today Carlos will be late, but no one has posted anything.
**Josh Suereth** 03:01 Does anyone use the hotel vacation calendar at all?
**Tigran Najaryan** 03:07 Like that? Where is that? Where is that? Where is that calendar?
**Josh Suereth** 03:11 I've I've heard it exists. I don't know where it is. Someone mentions it every time we're like there are people on vacation.
**Reiley Yang** 03:18 Yeah, there is a calendar, and I'm not using it. Because in Microsoft we're not allowed to do that like we can only tell people we're we're going to be on vacation. But we're not supposed to specify the exact range of the days, because the the worry some hacker might notice you're on vacation, they start to do something bad.
So so we have a policy. We we discourage people from making that public like. Normally, what I do is, I'll I'll just like Tell tell friends, and like, tell people in the private chat for people who work with me closely.
**Josh Suereth** 04:00 Okay.
**Reiley Yang** 04:03 Hey Carlos.
**Carlos Alberto Cortez** 04:06 Hey! Hey!
**Reiley Yang** 04:10 Maybe we should start. Bogan is not here, so I I can run a meeting. I'll share my screen.
Let me know if you can see it.
**Josh Suereth** 04:26 Okay.
**Reiley Yang** 04:32 Okay, so first, st Josh.
**Josh Suereth** 04:36 Yeah, this one might be hard without enough of us here. But I would just. We're we're kicking off the, you know, responsibilities and rotations stuff and the I I feel like for security right now. The way that's working is you look at the audit logs.
And you check like what's open. Right? So Armin Armin can speak to this. But you you check what's open? Make sure that there's progress being made.
I'll just say, the the overall theme that I'm thinking of is, maybe it makes sense for us to kind of hand over our rotations. Going forward. We talked about having, like one.
you know, one person responsible for rotation. I don't know how we all feel, but I was thinking, you know, there'd be when you, when you go on rotation. There's a handoff explicitly where you meet and chat, or whatever talk to the person I know. Armin and Carlos did this talk about what you were doing, if, like, you were in the middle of a release. And you had problems but for security specifically be like, Hey.
here's the things that are still active you should pay attention to. Here's the things that you don't have to worry about, just to make it easier as we pass things around.
I was also thinking about having that handoff. Maybe we could do it in this meeting as one of our triage points in the in the beginning of just do a quick handoff and and change the rotations to be Wednesday to Wednesday.
so that we're all aware of like, who's responsible for that week, but that's that's an optional thing, anyway.
**Tigran Najaryan** 06:18 Do we need? Do we all need to be aware of what's going on there, or only the 2 people who are doing the handoff.
**Josh Suereth** 06:24 It's only the 2 people being the handoff. It's just I was trying to figure out how to make sure we all have calendar time to do a handoff, and that we're not fighting to schedule additional meetings all the time.
Good armis.
**Reiley Yang** 06:36 Oh!
**Armin (Dynatrace)** 06:36 I don't think that we would need to have a whole lot of synchronous discussion. I think in most cases it should be sufficient that when whenever person a wraps up their their Friday in their time zone, that they would just leave behind a message.
either in the Tc. Channel, in case someone would have to take over person B's shift, or whatever, or in the DM. But maybe the Tc. Channel makes more sense, and then the other person picks up from there on Monday.
I don't think we need a synchronous meeting for it. It's.
**Tigran Najaryan** 07:13 Agreed.
**Armin (Dynatrace)** 07:14 Most things should be reflected on the ticket, anyway. On the advisory, and sometimes you have to chase maintainers on on slack when they don't. Don't see the notification in guitar. That's something that would then not be reflected on the ticket. And then you would just say, Hey, I talked to that that person from the maintenance group, and they promise to have a look if if they don't respond on the ticket, then reach out to them again. Please think that's all that I would put in the in the handoff procedure.
**Tigran Najaryan** 07:51 I agree, let's use the just. Let's use like for handoff. I think no need to do it all, you know.
in a call.
**Reiley Yang** 07:59 So.
**Josh Suereth** 07:59 That's great!
**Reiley Yang** 08:00 I have a very different opinion, and if you look at the this is something, maybe we should use a private meeting. But I I'll give you an idea. So so my goal is, I want Tc to be completely all from the security rotation. I think the security sake should be the one doing that. And if if we have Tc. Members who are passionate about this, they should also join the security sake.
and instead of herding the cat, and we have a group of people who look at the list of items and ping the Maintainers. Ask them to do the job. I want us to leverage the tool to automate the job and also have the escalation to the Gc. I want us to define what's the expectation for the Maintainers. Currently, I know, like Armin has been primarily driving that and also helping a couple cases where I reach out to the Maintainers.
They understand this is an issue, but they come back and say, but we have a problem. We're depending on that that component, that component is not owned by us. They have a security vulnerability, and I don't know what to do. So the issue has been there for a couple of months, and I feel like, if you want to drive something we 1st need to be very clear where we want to be like, we need to define the bar and communicate to the Maintainers. They know they know what to follow. The second thing is, I think the current security rotation from the Tc. Doesn't cover what we expect from the security sake. Like you have a repository. You have dependency on a lot of external things, and those things they have known security, vulnerability. You might be depending on something that has been there for 5 years, and people know it's vulnerable.
and you just don't fix it because nobody reads that to you. And in this rotation the Tc only ping people if someone filed a security issue like advisory.
But there are plenty of critical dependency issues.
So if nobody filed security advisory to your repository, are you okay? No, you're not okay. You have dependency on all these critical things have been there for for months, and they don't care about it. So I feel if the Tca. Is doing a really good job here trying to rally people and all the Maintainers just take care of the Security Advisory opentelemetry still has a huge issue with all the critical dependencies.
So what I want is, I I think we should systematically solve the problem. Instead of looking at the tip of the iceberg, and we should give the Maintainer a holistic view of from security side. What's the top priority that you, as a Maintainer, should take care of instead of their 4 different sources, and someone will just randomly ping you. And you don't have clear accountability.
I also think security is something that should be handled by a separate group, and of course, like we encourage all the Tc. Members to join. So I shared my perspective in the Gctc. Channel.
I shared that yesterday. So so take time to look at that and and see if you agree. I I feel the thing we're trying to solve from Tc. Here is not going to help open telemetry to improve security. We're just like being nice people trying to provide somehow here. But is that going to help open time should be more secure, I seriously doubt. So so one has to change the way how we work. And another thing is having having us being the man in the middle trying to look at something and pinging people. This is tedious. So we should like leverage tools to to automate this type of thing and hold people accountable through the contract.
And I have some concrete things I can share if later, like, we have time to go to a private session like I'll show you within open telemetry. There are many repositories that depend on certain components and the static analyzer, the scanners. They keep giving us this warning. We have a dashboard under the Github organization, showing us how many critical security vulnerabilities we have in the supply chain.
And Tc. Is like this is a blind spot. Tc. Is not covering that at all.
I'll stop here.
**Tigran Najaryan** 12:17 So what are you suggesting, Riley, is that we? We stop making the the responsibility of the Tc. With the rotations and all that stuff and move it to to the security sync, which I'm I'm totally fine with. Do we have the security sync and the membership in the security seek that is able and willing to take over of that responsibility.
**Reiley Yang** 12:42 Yeah. So I I already talked to the security folks. People are willing to handle this. And and this seems like we have good idea how to handle this systematically.
I feel the Tc doesn't have this like, we just have some existing process. We're following that. But we don't have people here proactively thinking about, how do you handle that systematically for this organization?
We're just like, Hey, there's a dashboard. There's some like advisory history. Then just go and look at that. But what about other problems? And why is this advisory the highest priority? Then we don't even care about the supply chain security when there's critical cves been there for months. So we need someone proactive thinking about it. So either Tca should be accountable for this or the security sake should be accountable for this. I want to avoid a situation where the security sake is looking at the security holistically across organization, where there's some existing thing that doesn't cover the entire thing, and only part of that. And there's a confusion about which one is the priority.
So my assertion is, if we don't change the way, how the Tc works on the current security rotation. Even if we do awesome job, all the Maintainers fix the problem on day. One open telemetry security still sucks.
and we have to.
**Tigran Najaryan** 13:55 Who do we have? Who do we have on 6 security right now?
**Reiley Yang** 13:59 So the the primary contribution was coming from me, and trust and we do help have help from Andrea and Jeremy.
They have. They have less control of the overall organization. So there are certain things they cannot see, and we yet have to define the process so to like in order to give them reasonable access to the system and Trust and I are the Admins. So we can. We can see a lot of things. And and we're building the automation tool to to improve the situation.
**Tigran Najaryan** 14:35 I'm personally more than happy to to do what you're suggesting.
Remove this to a specialized security. Seek. I think it makes sense.
**Josh Suereth** 14:47 So right right now. 6 security is mostly Microsoft, though.
like every every person you mentioned is Microsoft.
My! My fear like to to Tigren's question, Is it healthy enough to support this like? Is there enough investment from the ecosystem? And and I want to applaud Microsoft for like driving security in opentelemetry and thinking about it like, I think that's a good thing.
I think we have 2 options here going forward like one is, if it remains with the Tc. It forces us to all care about security, which I think we need to do.
But that said, I'm kind of with Tigran of having dedicated people who understand security are there. The the thing I kept hearing you say that was prioritization prioritization prioritization.
If it's a prioritization problem, who in open telemetry owns prioritization. If it's a what's the risk to open telemetry, the org, I would agree. A security Sig should be the ones that can actually like identify that. Well, I would want to see, like more representation from across the ecosystem there.
To make sure that that Sig is healthy, and I'll see what actions I can take to help out there. But that's my main concern with giving it to like. We know the Tc. Is relatively healthy right now in terms of size, and and folks that are sorry we are trying to increase the size. But we know that, like the Tc. Has a good representation across the ecosystem, and and we have things in place to ensure that happens right, Sig. Security. I would want to do the same thing for.
And I'd want to make sure there are enough people when you say it's you and Trask Dude Trask does everything in opentelevetry.
Does he like like? How much time does he have for that dedicated thing right? If we add to that, he's on the Gc. He's a Maintainer of Java. He's doing a bunch of things. It's the same as that's the same concern I have is, if the Tc. Owns it, you're like, Oh, the Tc. Doesn't have time to drive it right? The only person you mentioned who isn't on any other thing, I believe, was, was it Jeremy or someone?
**Reiley Yang** 16:53 Me on a drill.
**Josh Suereth** 16:55 Adriel's leading systems, or some kind of specification work, too. But that's fine, like I think you can do 2 things at once.
My point is like 2 of the people in there are active in a lot of open telemetry.
a lot, a lot of open telemetry, and one of the things we tried to do with like sponsorship limitations on the Tc. Was to avoid burning people out. So if we're putting this on that group.
is it. Is there enough people who can do the work to not burn folks out right and and and sustain it? Because.
anyway, that that's I like what you're suggesting. I think it makes sense to do that as 6 security. Let's try to make 6 security healthy as an ecosystem. I don't want to put a it's the same thing you're saying is like, will this solve the problem? If 6 security isn't large enough to handle that burden and we put it on them. We just burn them out.
So that that's that's my.
**Reiley Yang** 17:57 Can you? Can you explain what what burden are you thinking about? Is that the like? Looking at the advisory and ping the maintainers, or holistically look at the advisories and also the supply chain issue. Like all the Cbes.
**Josh Suereth** 18:15 I I think, tracking down. So so this is the way I think about on call at Google. And you can tell me how you feel about this? Our rotation on Tc around security is about triage and mitigation, making sure that things are running through to completion and taking an existing process. That's well defined.
Sorry, taking an existing process that's well defined and just making sure it runs.
And then, if there's an escalation, we're the ones that know who to escalate, to, who to get the answers from, and and we're just responsible for making sure it finishes the systematic replacement of architecture should not be the same people who are driving frontline responses to active vulnerabilities. They're the ones making the longer term decisions. They're building the infrastructure. They're building out like capabilities that we need systematically. If you put them on the front line, it takes away from their ability to build systematically. That's why, when we have like someone on a response to a vulnerability. Internally.
we don't have them on core work that has to deliver. We don't have them on core features. We actually give them dedicated time. A previous company. They called it surface work, right where you're there as a boundary to your team and making sure that you're resolving these things quickly so that someone else can focus on the core. So I'm actually more of a fan of making sure that the core work and the like. I have to respond to vulnerabilities quickly. Work are divorced, because what we don't want is if we suddenly get influx with a ton of vulnerabilities.
and the people who are working on systemic ways to reduce vulnerabilities are the same people. It means the systemic work has to pause and cannot continue, and you can't prioritize between the 2, because it's the same set of people that would be my concern.
I I find it real.
**Reiley Yang** 20:15 Yeah. So I, I agree with you. And we actually look at how other projects under Cnc operates. So the eventual goal is, we have a security response group. And that group is like it's different than the Tc. Or the security sake. But Tc. And security sake both should give guidance to the to the Security Response group. We're not there yet, because we don't have enough people.
and the idea is we'll we'll try to seed people from the Tc. Who cares about security a lot, and people from the security sake.
**Josh Suereth** 21:00 Yeah, I I like, so so what? What's our interim? Then?
In terms of how? Like, if our end goal is a security response team. How do we get there?
Do we give security response to Sig security? Now, do we keep it on? Tc. I.
Which what actions will help Us build a security response team.
**Reiley Yang** 21:21 Okay, so.
**Josh Suereth** 21:22 Question in my mind, yeah.
**Reiley Yang** 21:23 Yeah. So so my take is, I'm less worried about which team is doing the rotation. For now I'm more worried about how do we improve the current process because the current process is very broken in my mind. I'll give you 2 examples. First, st if someone had it to report a security issue on Github. They just send email that email would go to the security seek today. It won't get to Tc.
there's some existing email that still go to the Tc. Which I want to stop, but we have to align on having all this communication to the security sake or the Tc. Right we have we have to make a call. So the problem is, the Tc rotation is currently handling the advisories and the privately reported like email thing, go to the security sake and for the cves that nobody reported. It's just the underlying dependency anyone can use a scanner to realize. Oh, you have open telemetry, python, python. Depend on Http library, and that one has a critical security vulnerability. The Tc. Don't care about it right now. The security sake don't cover it right now. So there's a huge blind spot. And we're seeing this problem like being there for years, and it's getting worse.
So I I feel what's important is trust, and I worked on the the Cicd security. So you start to see like we, we try to make sure by default. You have read-only access.
and if you need additional access, you have to specify that in the Yaml file. The second thing is, you don't use a floating version of the Github actions. You have to ping the version.
The 3rd thing is, if you use something that's not widely used, or something that hasn't been maintained for years, let me go and remove that. Like the markdown link thing like we move to a better version that's maintained. Then for the for the software component dependency, there are 2 things. One is you might have, like python package, depending on other Pypy packages, or like Npm. For Javascript, or like New guide Fornet. The problem is one. We notice many, many of these components. They depend on another external component that hasn't been maintained for years. And this is why you don't even have Cve, because nobody cares about it.
Number 2 is you depend on some legacy component. Recently, we realized there are components depending on the 1.5 version of Aws, Dk, which has been deprecated for 4 years.
and there's no Cve on it.
So we want to do something holistically. We want. We want to let the Maintainers know if you have. Ci CD, problem like, if you use a Cicd flow that you don't have trust or by default, you gave it a lot of permission which you shouldn't. Then you have to be accountable for this. Go and make the fix. If you depend on a package that it's not widely used. It hasn't been maintained for 9 years. That's crazy. You shouldn't take dependency on that number 3. If you depend on a legacy component. There's published known cves.
You have to fix it. You don't wait for someone to file advisory to you. Number 4 is, if you have advisory, you got to take care of it in a reasonable manner, like with a timely manner. So these are the 4 things we consider very important for the supply chain security. So Trustw and I worked on the Cicd. That part is done. We also have the renovate and depend about so we can make it more automated. You start to see this like across the entire organization. Now, we're trying to handle the supply chain security, and we don't want to only rely on advisory because that's covering maybe 1% of the problem. And I want to solve that problem. So either the Tc can do this, then we have to change this. The Tc. Will handle both the advisory and the dependency Cves.
and we need to work with the Gc. To communicate to the Maintainer what we expect, or if the Tc. Doesn't have bandwidth to improve the process, the Tc. At least needs to align with the security sake by saying the security sake will define what's the new process? And the Tc will keep doing the rotation. But taking the improved process, that part is okay. So I'm not a big fan of moving things from one place to another. But I'm a huge fan of us, taking care of security in a way that it really helps security. So we keep running an existing process without even thinking about whether it can help or not.
And the last thing is a container image. We do publish container, image, and those container images. They depend on some legacy version of whatever Linux they have security, vulnerability, and we have to do the due diligence there, and we have to deprecate the old version that has no vulnerability. So we want to give this guidance and hold the Maintainers accountable, then Tc. Security, like rotation, whoever doing that they can be hold accountable of rallying people.
**Bogdan Drutu** 26:37 I have a question.
what is the purpose of this conversation? I'm trying to make sure we at least take some action items out of this like we are not having this conversation just to have it, because I feel like I heard these complaints and all these good things before, and we didn't take any action out of this.
**Reiley Yang** 27:01 Yeah. So so my, my ask for for this group is currently we're we're running a process. We're running a rotation. But we don't have energy to think about whether this process makes sense or it help open telemetry security. And there's a huge blind spot, and the security is trying to improve it. So we need a model for these 2 groups to work, or we just consolidate that to one group, let one group deal with that.
**Josh Suereth** 27:25 So, Riley, what I'd encourage you to do. Then write this down and make a proposal like.
I've heard this from you a few times, and and I again I applaud you for pushing on security. But like, make a proposal right like. Let's to Bogdan's Point. Let's let's start moving on it. If we want to improve how we do security rotations. The last time we talked about this it was cool. What we have isn't perfect.
but we can't just drop it. So what's the next step like? If you want to move it to 6 security.
let's make a proposal. Let's talk through it. That sounds good. That should be the next action. But like let's write it down, and let's make sure some of the concerns you have. Let's document. If we can have concrete examples that are safe to share. That would also be ideal right.
So. Yeah, but I I think at this point I don't hear anyone complaining, so let me know if I'm speaking on like 2 forward. But I think we're at the point. Let's evaluate a proposal and move forward on it as opposed to like. Discuss what we want to do.
**Bogdan Drutu** 28:35 Yeah, I'm and I'm happy to support it, like, it's just like, I want to have more action driven discussion.
**Reiley Yang** 28:45 Yeah, I already have a draft proposal. I'm going to send that out this week.
**Bogdan Drutu** 28:48 And maybe maybe ask Gc. If they want to have the proposal, or they want to own the, not the proposal, the action item out of that, because it may be them that they should own the action item out of your proposals.
**Reiley Yang** 29:03 Yeah, I'll already notify the the Gc. About this.
**Bogdan Drutu** 29:25 Okay, Josh, you have the next topic. I think.
**Reiley Yang** 29:30 No, I have the next so essentially the same, like the the supply chain security. So as I covered the 6, security has identified the following things like Ci, CD, the package level dependency, the container base image like Linux, whatever dependency, and the the tool chain, like the compilers or something that you use. So we want to improve this overall. And and instead of giving people like multiple things without a clear priority, we want to give give the Maintainers one single thing. So the current idea you will see that in my proposal is we want. We want to have a public dashboard for the Maintainers like for each repository, we let him know.
Is there something burning that you should take immediate action, which means you should take action before the end of the week, or it's something like it's coming. You don't have to take immediate action, but it'll be a problem if you don't finish that by the end of the month. So we just want to give this very actionable item to the Maintainers and and we'll we'll discuss with the Gca. My.
my current thinking is, we probably will spend 5 min in the Tuesday, like Week Weekly Maintainer and spec meeting, just to show people where we are, and in that way to hold maintainers accountable.
So the public one will just tell you, as the owner of a certain repository under open times. Do you have action item, and what's the due date? And it doesn't have additional detail because it's sensitive. Then you can click a private link if you have the access as a Maintainer. They can see what's the concrete thing in this way. We don't have a group of people in the middle trying to rally people.
Okay, so that that's my topic.
Oh.
**Bogdan Drutu** 31:39 Same same question, what is the action item, Riley? I wanna make sure. Since I'm putting on call to document this, I wanna make sure we document exactly what is the action item we are looking for for this.
**Reiley Yang** 31:54 Yeah. So so before I have a, I have a proposal out. You don't worry.
You do whatever you're already doing, like. We already have a process. Just keep doing it. Once I have the proposal I'll share, I expect, feedback from both the Tc. And Gc.
**Bogdan Drutu** 32:11 Okay, before the proposal that.
**Reiley Yang** 32:32 Yeah, then, I know we used to have some private topics, but.
**Bogdan Drutu** 32:36 Okay. But for that, we need to switch the zoom link any other things. Public document discussions. We need to have.
**Josh Suereth** 32:50 I I was. We can talk about this later, I'm thinking, with the with all of us attending the specification meeting with the rotations and things that are happening and more offline discussion. I do want us to consider reducing this meeting to bi-weekly or sorry every other week.
To kind of reduce some meeting load that said.
if we continue to fill our topics with 1 h of content every week, I'm not going to propose that yet, but I want it on our radar.
**Bogdan Drutu** 33:24 Yeah, I I think it's a good idea.
do. We still want to have the Gctc. Meetings every other week?
**Armin (Dynatrace)** 33:36 That one we have monthly right now, I think on like second Wednesday of the month, or something that's a good cadence, I believe.
**Josh Suereth** 33:50 Cool. With that we can go to private.
**Bogdan Drutu** 33:52 Who who is going to generate the link.
or or I think it's in the Channel. Sorry it's in the Channel bookmark somewhere.
**Josh Suereth** 34:01 Okay. See you all over there.
