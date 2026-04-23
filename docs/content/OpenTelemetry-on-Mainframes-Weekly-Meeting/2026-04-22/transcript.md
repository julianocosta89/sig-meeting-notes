SIG: OpenTelemetry on Mainframes Weekly Meeting
Date: 2026-04-22
Duration: 32 minutes
============================================================

## Zoom Recording Transcript

**Ruediger Schulze (IBM)** 01:21 Hi, Greg. Thanks for… for… I'm still… I'm still… there's a GSE background. Okay.
**Greg Shriver** 01:31 Megan, how are you?
**Ruediger Schulze (IBM)** 01:32 Yeah, good. It's busy times. Obviously, what I did today.
**Greg Shriver** 01:38 Yes, yes, I can. Yes, I can.
**Ruediger Schulze (IBM)** 01:41 Okay, good.
**Greg Shriver** 01:45 had a chance to review the Federated Semantic Conventions Lifecycle proposal that you… that you sent out.
So… Yeah. That makes a whole lot of sense.
**Ruediger Schulze (IBM)** 01:57 Exactly.
**Greg Shriver** 01:59 And it also begs the question that You know, perhaps mainframe.
Should be its own federated.
**Ruediger Schulze (IBM)** 02:11 Exactly, and actually, this is the case. So what… I kind of, like, tested this on Monday on the semantic convention stick call.
So, as you can see, right, this is a… this is an OTAB, this is still a little bit in…
**Greg Shriver** 02:24 Sure.
**Ruediger Schulze (IBM)** 02:26 But the Gen AI… and based on this, you can also see the scale, so the Gen AI SIC, they are probably the first one to go into a federated approach for…
**Greg Shriver** 02:39 sense.
**Ruediger Schulze (IBM)** 02:39 Teams?
And, I asked this, actually, how that should be. So, they would be still a repository on the OpenTelemetry.
So, you know, full visibility within the project scope still given, and I think this is something that we should be doing as well. It will imply that we need to get a backer repository. We had one earlier, but obviously we archived that one. This was also more.
**Greg Shriver** 03:07 Yeah.
**Ruediger Schulze (IBM)** 03:07 specific. We probably really want them to be clear on… how we want to name this, but I would actually… I see a lot of value in this proposal.
**Greg Shriver** 03:22 I do too.
**Ruediger Schulze (IBM)** 03:23 And, I also see it in a way that it probably will allow us to accelerate in this space.
**Greg Shriver** 03:30 I would agree.
**Ruediger Schulze (IBM)** 03:32 And, It's probably… another couple of weeks out, but I would model what we want to do based on what the GenAI SEMConf is doing, and really try to get this started.
**Greg Shriver** 03:52 Do you have a link to that, Rudica?
**Ruediger Schulze (IBM)** 03:54 They don't have a link yet.
**Greg Shriver** 03:56 Okay.
**Ruediger Schulze (IBM)** 03:57 They are just about, really, also getting into this space. But, I think we should follow this, and then really get things going, and… and… make also this secure operational in the way that we manage these semantic conventions, and how it's being described in the OTAB, but I see a lot of value that this is actually then accelerating of what needs to be done.
**Greg Shriver** 04:32 Yeah.
Yep, go ahead, sorry.
**Ruediger Schulze (IBM)** 04:35 And the tooling, actually, is there to help us, as was also mentioned in the OTEP, and I think this… this will then… give us, presumably, some cadence of how we can make these definitions in a more efficient way, and probably also unlock some of these discussions. It raises some questions on namespaces, obviously. It also raises the question of how we want to deal with virtualization. There's nothing there for virtualization.
Is this the question, should we just run this on our own, and then lack of nothing available, right?
But, I… I think it's… for the good, for the platform, it's definitely… let's have, kind of like, for the mainframe ecosystem, our… our mainframe domain have… have the definitions being driven forward, eventually.
If we have a model for virtualization and being covered that is mainframe-specific, and at some point the community is maybe further And virtualization, maybe we retrofit or whatever, right?
**Greg Shriver** 05:48 Right.
Yeah, Well, I mean, if you go to the end of the, the link that you provided, I mean, there's… there is… a non-trivial list of still-open questions, right?
And, I mean, but everything that's laid out in the beginning makes 100% total sense.
It seems to be pretty well thought out. I don't know when this thing started, but… .
**Ruediger Schulze (IBM)** 06:21 On that one, I think this was ongoing for a while, the… while I… so far, because it was also never really… surfaced in detail, at least not on the SIG meetings where I was on, on the semantic convention SIG meeting where I was on. I think they talked… they mentioned it a couple of times, and throughout, probably, at least this year, but I think now it's at a stage that this is really surfacing and getting into practice.
**Greg Shriver** 06:49 Yeah.
**Ruediger Schulze (IBM)** 06:50 What we should try is actually to hook on this and… get these different contributors of the SICK to really work on this.
And, Then we need to look at, you know, how we do this with versioning, and we probably need a time as well to… to get into it, but.
**Greg Shriver** 07:15 Right.
**Ruediger Schulze (IBM)** 07:16 I think this would… Would help us from a platform perspective, definitely.
**Greg Shriver** 07:22 I… I completely agree.
I mean, it looks like we're gonna have to intersect with the… with the core semantic conventions at some point, and… and even in one of the… in one of the open questions, I think they made the statement, like, well, how do we prevent, you know, namespace collision across federated repositories And, And I think the statement was made in there that there would be one central repository that has a link to all of the federated repositories, so you can't just invent the federated repository.
Right. Or a federated convention, actually. Maybe repository is the worst word, because they did say… another open question was, they don't know where it's going to live. Are they going to be separate repositories? Are they going to be shared repositories? But, you know, the conventions themselves would be federated.
So…
**Ruediger Schulze (IBM)** 08:20 Do you… So, yeah, so what I assume is, and this to be verified, but we claimed already some namespaces.
Sure. So, I assume that we could build on them, and that they probably will find, you know.
a place in the existing, or in this new namespace repository, or regret.
**Greg Shriver** 08:47 It was true.
**Ruediger Schulze (IBM)** 08:48 To say.
**Greg Shriver** 08:48 Yeah, the registry, yeah.
**Ruediger Schulze (IBM)** 08:50 what I wonder is, and this is something we need to probably discuss, I think we claim mainframe right now, we claimed COS right now, we claimed TPS.
All this TPS discussion wasn't too successful.
**Greg Shriver** 09:05 Right.
**Ruediger Schulze (IBM)** 09:06 We can still try to drive this forward, but maybe we should… be… maybe it's USTPS or whatever, right? We probably… also in our… also in our own interest to make progress, we probably should be very pragmatic on the namespace.
And, the way I understand this, and I think we will see this, essentially it would imply that everything that we do lands just in, you know, what we do for the domain lands under this namespace.
**Greg Shriver** 09:38 Sure.
**Ruediger Schulze (IBM)** 09:39 And, that would also imply things like processor type. It would not, you know, fiddle around with the base semantic conventions on… Is this… is there an attribute, process, or type? Would these values be allowed? I think it would be more… We define them… A processor type for the mainframe, and we can do there what we want.
**Greg Shriver** 10:07 Right.
**Ruediger Schulze (IBM)** 10:07 That's the model. And I think this is how we should… actually start… get these things going, and then use the tooling, and if it's… Progressing, and if the sick, our sick, is agreeing to the approach, Then, it's probably the way of how we want to move forward with…
**Greg Shriver** 10:30 Yeah.
Yeah, I would agree.
So you're suggesting that we use the tooling and basically come up with, like, a stub, a mainframe stub.
Semantic convention, and just start building it out from there, and start with a really thin slice And then… build it up.
**Ruediger Schulze (IBM)** 10:51 Right, right.
**Greg Shriver** 10:53 Yeah.
**Ruediger Schulze (IBM)** 10:53 So…
**Greg Shriver** 10:54 I mean, it's not unlike what we've already discussed about taking, like, little pieces, but it does… it seems to make the problem feel more tractable, right? Because it's smaller.
**Ruediger Schulze (IBM)** 11:07 Yeah.
And also, you know, I think we can go the same way what we discussed throughout, you know, these last months.
Let's take what the HMC provides.
Let's have a… and I think we even had a spreadsheet for this at some point. Let's… let's translate this into something that You know, everybody can agree from this sig to… as a representation of how we would represent CPU times, or CPU utilizations, actually, how we represent processor types, how we represent, Maybe there's something about adapter cords and so on, right? And then build it up the stack. If we talk about LPOS, how would we name the… the utilization on the helper, how would we name… yeah, it comes back to resources and entities, so… but this is where the tooling supports, because we anyway need to follow the same mechanism as in the base semantic conventions, so… we actually… Would be in control, was what the community is doing.
And, that hopefully would speed up, and we don't have these discussions with the semantic convention sake, does it fit or not? Should this be different or not? I mean, obviously, we should be learning from their best practices.
**Greg Shriver** 12:30 Yeah.
**Ruediger Schulze (IBM)** 12:31 To… to adopt, but, on the other hand.
If we as a SIC, and I mean, obviously, you know, primary vendors are obviously participating in the SICK, I think it asks for these vendors to… to really validate, then, what is somehow making it into the… into these conventions, but if we agree, then I think that's… That's the way forward, right?
**Greg Shriver** 13:01 I agree. I mean, I think that… just the pro… just the… the fact that we're… that we're entertaining federating this, it's not going to eliminate all of our alignment issues. Like, for example, I mean, one that seems to keep coming up is… Is… we can't have a million attributes. We can't have a million different entities. Because… We… it… the… the instrumentation will not be able to… Generate all of that in a performant way, and people won't use it And… and when you say… you know, you made the statement, like, well, maybe we take, you know, something from the HMC and generate this.
And I… I mean, I think that's a great start, but I'm actually thinking that maybe something that actually makes it to the OpenTelemetry subset might be a subset of that, right?
We'd want to make sure that we don't, like, collide with anything that's coming from, you know, something like the HMC, but at the same time, do we need… how many metrics actually are… how many… how many entities would come from the HMC? I would think many, right?
**Ruediger Schulze (IBM)** 14:21 Yeah, that's a… that's a fair point. I mean, on… yeah, on the other hand, when we do this exercise, it gives us kind of, like, you know, at least a clear specification, what is an LPOR, right?
You're right. Heck, that allows us at least to model the lower layers. Would we have?
I think we really should keep it… but this is maybe part of the exercise, keep it tiny to it, you know, To a certain subset of attributes which are… identifying, maybe not so many descriptive attributes, I think… That might already help. And, yeah, and then obviously, Looking at these things that are really, really necessary moving forward.
Right.
Yeah, so this was… but I'm actually glad that you agreed to this approach. I don't know if somebody else was on the call earlier, I couldn't make it today on time, but… I think what this boils down to is essentially when the Gen AI made their first move, we make our move as well, and we… we really need to then ask the… the… any participants of the… of the SICK to, Validate, or kind of, like, concur that they.
**Greg Shriver** 15:54 They're…
**Ruediger Schulze (IBM)** 15:55 Do this initial approach, and then we can ask, you know, let's… let's contribute what, you know.
And we have topics, HMC spans.
a couple of vendors have been working on spans, I think. A couple of vendors have been working on metrics, let's start from there.
And then… I think, in fact, it boils down to more the SRE type of use case, or what makes it actually… it's not… probably you don't need to have an OTEL semantic convention for something that anyway only lives in the mainframe context.
Just an assumption, but, it's probably more about what goes to… to any… I need it.
Consumer in the, in the organization.
Okay.
While we speak, Craig, and I apologize, I also didn't make any progress on… I still have a couple of comments on the… on the document. Where are we actually with this, Okay.
**Greg Shriver** 17:08 Yeah. You saw my face, so basically… and it's a time problem.
**Ruediger Schulze (IBM)** 17:12 Yeah, it's just…
**Greg Shriver** 17:14 Just a time problem.
You know, my next… my next… My next steps are to… Are to, you know, still investigate the use of those code spaces.
So that I can get those… those workflows to work.
Yeah. And I, I just, you know, I haven't.
And I know, I know that's… that's kind of blocking the dock PR, right? But… But yeah, I haven't… I haven't made any progress on it. Again, I need to apologize as well.
So… I guess, you know, the prior comment that you made, like, that you didn't… you don't know who joined in the beginning, I don't know who joined in the beginning either, because I didn't think that anyone was gonna join You know, so I just… I… I posted on the chat, on the Slack channel that, you know, hey, I'll… I'll join at plus 30.
**Ruediger Schulze (IBM)** 18:12 I see. Add-on.
**Greg Shriver** 18:14 Yeah, I don't know if anybody else joined before that or not. I put some meeting notes in.
But…
**Ruediger Schulze (IBM)** 18:22 Idle.
**Greg Shriver** 18:23 I… I doubt anybody joined, and if they did, they didn't… they didn't… they didn't put it in the, They didn't put it in the notes document.
**Ruediger Schulze (IBM)** 18:33 No, that's fair. I only realized that the code spaces seem to work again.
You know, remember when we had been on the call, it somehow didn't work. I believe this was maybe a temporary issue.
**Greg Shriver** 18:48 Okay.
**Ruediger Schulze (IBM)** 18:51 I will still make a couple of comments, hopefully, tomorrow. I have another session on this UK Virtual Conference tomorrow, and once I'm done with this.
Okay. Should be a little more free again.
I have a couple of more comments on the… it's just about wording on the… on the… on the article.
And then.
**Greg Shriver** 19:13 Okay.
**Ruediger Schulze (IBM)** 19:14 Yeah, it's really about fixing those formatting issues.
Maybe we can move.
You know, anytime, then release it.
And then I would suggest, let's focus on Giving this, federated approach priority.
**Greg Shriver** 19:35 I would agree.
**Ruediger Schulze (IBM)** 19:36 And, then, you know, it becomes a discussion just within this group to make progress.
**Greg Shriver** 19:45 Yeah, for sure. So, to be 100% transparent and honest, I was unaware of this federated semantic convention's lifecycle at all.
Until about a half an hour ago, you know, because you posted this, I went and I read it, I'm like, well, this makes perfect sense. One of the things that I have not done is I have not vetted this within our organization.
Right? I'm thinking, I don't know, you know, what kind of feedback I'll get from here. I don't think we'll see any pushback, because I think honestly, I think everyone will… my guess is that everyone will agree that this is, you know, this represents an opportunity to move this thing, to accelerate this.
You know, because if we don't, then it's… You know, eventually it's just gonna die on the vine, because there's so much friction, right?
I think this is a, So, I guess, you know, without putting too much in there, I will… You know, at least increase the… I'll socialize this within our organization to see if we can get some feedback, you know, at least across Broadcom, so…
**Ruediger Schulze (IBM)** 21:00 Yeah, yeah. And from our perspective, We… actually, we want to make progress with the semantic conventions this year, and.
**Greg Shriver** 21:11 No.
**Ruediger Schulze (IBM)** 21:11 I think it's not actually changing something, right? It's just where you put the conventions and how you… how you actually agree to them, but it's not changing the… the target. The target is still the same, and eventually, as is written there, if we once are super stabilized, we could actually become part of the base again.
**Greg Shriver** 21:38 Yeah, if… I noticed that as well in some of the open issues. They said that, You know, for some niche things, you may want to stay federated forever, and for others, they may want to actually, you know, graduate and promote into the base sumconv, so, you know… I think we're a long way away from that.
**Ruediger Schulze (IBM)** 22:01 And I would actually rather promote the… You know, and I think it would… I mean, where this is going, right? I mean, the community, they started also, there needs to be implementation of conventions that go in, but I think, realistically, we're in a slightly different world. I think we should be agreeing these conventions.
And then every vendor can go off and implement them, get also this model supported to test this, there was this URL that you… schema URL that you should be having in your… in your instrumentation, and then… I mean, ideally state would be if, even in the sick, we come to this point that, you know, the different vendors would maybe say.
Okay, we are supporting a certain version of this mainframe domain.
**Greg Shriver** 22:51 memorized.
**Ruediger Schulze (IBM)** 22:51 convention. I think this would be already… Quite helpful, for the ecosystem, yeah.
So…
**Greg Shriver** 23:01 I would agree.
I would agree, and I think, you know.
You know, did they talk at all about cadences?
**Ruediger Schulze (IBM)** 23:10 No.
It's completely up to, to the, to this domain, then.
And actually, this is the point, right? They decouple this, because this is what they do about the major versions. So, if either or would go for a major version, you are not impacted anymore, or you don't need to be stable, or… I think it's more than for us as a Sikh to… Kind of, like, get to this, you know, first of all, the mechanics, and then secondly, you know, somehow agreeing when is something stable or not.
**Greg Shriver** 23:49 Right.
**Ruediger Schulze (IBM)** 23:53 There's also a couple of terminology things, but this is also… maybe I may have inter… we may have dissimilar discussions, right?
and what we discussed also, right? The sysplex, this is a cluster, or this is a… how do you call this the sysplex thing, right?
**Greg Shriver** 24:11 Right.
**Ruediger Schulze (IBM)** 24:11 This is maybe more where, from, you know, the ecosystem, at some point, maybe we need to source feedback.
But this can be beneficial, right? So, to… To finally get also conclusions on how to name these things.
**Greg Shriver** 24:27 Sure.
**Ruediger Schulze (IBM)** 24:29 Right.
**Greg Shriver** 24:30 I mean, yeah, there's… there's… You know, they talked about namespace collisions across federated repository, or federated schemas.
But, you know, there's also concept collisions across, you know, or duplicate concepts across federated schemas as well. And, you know, the namespace one's probably pretty easy to deal with.
you know, the, especially with the automation and the registry that they're talking about, and also the platforms, which I thought was pretty… pretty ingenious, you know? These are all… these are all… these are tested together.
But, the… The concepts, you know, like virtualization, what's a cluster, what's a this, what's a that, that's… that's harder.
**Ruediger Schulze (IBM)** 25:18 Yeah.
And this is maybe also where my biggest question is, right? I mean, do we just do something from a mainframe point of view for virtualization? Right.
And then it would live under this namespace, and then at some point we merged back, but then again, we have this trouble, right? So… Sure.
But I… yeah, I… so I will try to follow the semantic convention sig whenever I have time, and .
**Greg Shriver** 25:50 I'm glad that you did. Is this where you learned about it? I mean…
**Ruediger Schulze (IBM)** 25:53 Yeah, it was actually because Monday I had, after a long time, time again to join it.
And actually, these sick meetings, or yeah, I think this is the best way to learn things. You can, of course, try to follow the read… to read the old tabs, but… Or sometimes things are posted on LinkedIn, when there are really cool things happening.
Then, you might also see a LinkedIn post, but… It's actually… best thing is actually the best information you get when you occasionally join these Sikh meetings.
**Greg Shriver** 26:29 Yeah, for sure. Well, I'm glad you did.
**Ruediger Schulze (IBM)** 26:32 Yeah, thanks. Right. And, the… Yeah, let's… let's… let me ask this, you know, once these things kind of, like.
What I would do is, I think I… so I… probably on the TPS, I don't… so last time when I was on the SIG meeting, right, they still said, you know, write a blog about TPS, get others engaged. I think I'm moving away with this. I would actually… I would say, okay, Let's not spend time on this.
Let's do our own thing for now.
we actually want to make progress. Even this would require that the kicks team needs to rename their spans.
as a follower on this, but maybe we reach a point, maybe if maybe this SIC here, as a community, reaches this point that, you know, this band should be named like this, right? Whatever we decide.
Or unless, you know, TPS may be the thing to move forward, then okay, then let's agree to move forward with it. Then we need to probably go for another namespace, right?
manage multiple namespaces is probably something which we also need to be clear about if we want to do this or not, or should be doing. I think this is a question which, at some point, I need to ask at the semantic convention SIG meeting, but I think nobody is yet there at this point. Also, I have to say, on Monday.
one of the Kiki players, he had to leave after half an hour after he introduced his OTEP, and then with the other one, I raised a couple of questions, but there's a few other people that, if they would be on the call, it's probably… Then also good to understand the perspective of how things should be done.
And it's probably also something among this group here to then decide, you know.
are we okay with Mainframe as the top-level namespace? How does the US play into this?
Yeah, right.
But, I think it will help, and in fact, I think it will help in the end to make progress.
**Greg Shriver** 28:56 Yeah, I agree.
**Ruediger Schulze (IBM)** 28:58 Right.
**Greg Shriver** 28:59 I agree. All right.
**Ruediger Schulze (IBM)** 29:01 Okay, good, Craig, appreciate the time that you, that you came for.
I still need to see how it's next week with my time. I'm traveling next week, again.
But, I think this is… this is really an important thing that can help us.
Yeah.
**Greg Shriver** 29:23 I agree.
I agree. So, you're out… you're out next week, I should be able to join next week, and, you know, I… We can have a discussion You know, a further discussion on this, and also sort of the relative priorities that you were talking about, like.
you know, get the outstanding, outstanding, PRs.
You know, the open PR is the, sort of, the disposition of those, and then after that, would really like to, you know, prioritize moving forward with this federated semantic conventions lifecycle stuff.
That's all.
And, you know, hopefully everyone will have had a chance to take a look at the OTEP, by then.
**Ruediger Schulze (IBM)** 30:17 No.
Okay.
Yeah, next week I'm out, and… Next week is already 29th, right? Yeah.
A sh… 6, I don't know yet. 6 of Maya, I don't know yet.
It's busy times, obviously. Maybe we need, at some point, For a better time to…
**Greg Shriver** 30:37 Yeah, I was thinking that as well, because we already changed the time, right?
**Ruediger Schulze (IBM)** 30:42 Yeah.
**Greg Shriver** 30:42 But that hasn't really seemed to help. In fact, I think the time change that we made actually made things more difficult for you.
**Ruediger Schulze (IBM)** 30:49 Yeah, yeah, this is because somehow, you know, there's always overrunning meetings.
**Greg Shriver** 30:55 Yeah.
**Ruediger Schulze (IBM)** 30:56 Easier if it's later.
**Greg Shriver** 30:59 Next week, I'm okay. I'm also okay the following week on the 6th.
I should be okay, unless something horrible, dastardly happens.
**Ruediger Schulze (IBM)** 31:13 So maybe the next two weeks, even if I don't join the meeting, maybe we try to work together of getting this documentation, PR out.
And, if you have any questions, just ping me. We can also jump on a call to… just, resolve the… the questions, if this…
**Greg Shriver** 31:31 We've talked… Okay.
**Ruediger Schulze (IBM)** 31:33 Obviously, right.
**Greg Shriver** 31:34 I'm sorry, what were you… were you suggesting not to have the SIG meeting, or.
**Ruediger Schulze (IBM)** 31:38 No, I'm suggesting to have the Sikh meeting, but I would… if I not join, right, maybe we anyway can close the PR working on Slack together, and…
**Greg Shriver** 31:48 Yeh?
**Ruediger Schulze (IBM)** 31:49 solving this. And then this is off the table, and I think it's also a good thing if this… If the mainframe is represented on the OpenTelemetry page, actually helps as well.
**Greg Shriver** 32:03 For sure. Yeah, I would agree with that. I would agree with that.
**Ruediger Schulze (IBM)** 32:06 And, I mean, I… the fun thing is I can… I can open a PR against your PR, because I can't hate it. I may open a PR against your PR, you have to approve it and…
**Greg Shriver** 32:27 That's funny, yeah.
**Ruediger Schulze (IBM)** 32:29 Okay, okay, great.
**Greg Shriver** 32:32 Right.
**Ruediger Schulze (IBM)** 32:32 Yeah, thanks a lot. Thank you.
**Greg Shriver** 32:35 Click.
**Ruediger Schulze (IBM)** 32:35 Bye.
**Greg Shriver** 32:36 Yep. Thanks, Rutica. Bye-bye.
