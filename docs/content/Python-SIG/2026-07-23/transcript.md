SIG: Python SIG
Date: 2026-07-23
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Riccardo Magliocchetti** 00:16 Hello.
**Tammy Baylis** 00:21 Hey, Riccardo. Hi, Radhika.
**Aaron Abbott** 01:39 Everyone, how's it going?
**Tammy Baylis** 01:44 Hey, Erin. Hey, everyone.
**Aaron Abbott** 01:47 Looks like everyone figured out the new Zoom link.
**Dylan Russell** 01:55 seems to work.
**Riccardo Magliocchetti** 02:17 So welcome, everyone, to this week's Python SQL.
In the meantime, we wait a few more minutes for more people… for more people to join. Please add yourself as an attendant to the notes, and also feel free to add any topic you want to discuss. Thank you.
And please, when you add notes, topics to the notes… Please also prefix with your name, so… It's easier to know.
Thanks.
Thanks, Radhika.
Okay, people, I think we can start.
Tammy, do you want to do the triage?
**Tammy Baylis** 04:31 Yes, please.
Sharing… Cool.
Alright, looking at the board, we'll just look at a few no status to start, and we'll stop at 9, 10, or in 5 minutes.
Handle encoding exceptions in OTLP exporters, open June 10th.
Based on a recent issue from Lukas… Hector has already added some suggestions, but this is on hold.
for… A moment.
We'll leave that there.
Fix, metrics, convert list attribute.
values to… Tuples for aggregation key.
Related to… Oh, kind of an old issue.
**Lukas Hering** 05:39 I think we went through this last week as well.
**Tammy Baylis** 05:41 Yeah.
**Lukas Hering** 05:42 By Dylan's PR.
**Tammy Baylis** 05:45 Yeah.
No, it's stale, so we'll leave that.
Maybe I… maybe I should go bottom-up next time?
Yeah, I'll look at this one, then I'll try bottom-up next time.
Don't rush… Linked to an issue… Last year… Yeah, I think this looks familiar, too.
Yeah, we asked. Okay. Note to self, go bottom up.
**Lukas Hering** 06:25 I don't know, can we move those 3 to the bottom, maybe?
**Tammy Baylis** 06:31 Yeah, how do you do that?
**Lukas Hering** 06:36 Maybe not.
**Tammy Baylis** 06:39 Hmm.
Yeah, I… I suspect, could be wrong, but I think these are, like, Most recent activity at the top, and then…
**Aaron Abbott** 06:50 Yeah, I think there might be a sorting control in the dashboard, like, on the right.
Yeah.
**Tammy Baylis** 06:59 Hmm…
**Aaron Abbott** 07:00 Yep.
Yeah, that one's sort by, yeah.
**Tammy Baylis** 07:10 Sort by updated… Here we go… Oh, not that way.
Updated, descending… Okay.
Cool, okay, cool.
Thank you.
Oh, very fresh, from Dylan, an hour ago.
**Dylan Russell** 07:40 Yeah.
Yeah, this one, I made a mistake when I moved the GCP resource detector over.
And I…
**Tammy Baylis** 07:50 Hmm.
**Dylan Russell** 07:51 Let's change the directory structure.
Which I didn't mean to do.
My agent did it.
So, this is just changing.
**Tammy Baylis** 08:03 Director.
**Dylan Russell** 08:04 Great structure back to what it was.
Which doesn't match what we do in this repo.
But… So that's maybe the one question to discuss on this is… How much do we care that it doesn't match?
What's in the repo?
Which… I think what's in the repo is it'll just be source open telemetry… Slash resource slash detector.
**Tammy Baylis** 08:37 Instead of that.
**Aaron Abbott** 08:40 the PyPi package name is also hyphenated.
For, I think, the AWS one.
Whichever other ones we have is, like, resource-detector, which matches the… The dots in the import path, too.
**Dylan Russell** 08:55 I see.
**Aaron Abbott** 08:57 But I propose, since we didn't, like, intend for this, we should… yeah, like, exactly this PR, and then maybe we can… This one's already independent version, so if we want to break it to match the repo import paths, I propose that we do it with, like, a… Major version… bump.
But honestly, it doesn't seem like a big issue to me. This obviously was a disruptive accident, so…
**Tammy Baylis** 09:24 Yeah… Okay, I'm going to change it back in this… PR… I can discuss names, spacing, and major release later.
And that's ready for review.
Thanks, guys!
-Oh, add crew AI instrumentation… I think it should go in the other repo.
**Aaron Abbott** 10:00 Maybe we were discussing this one in Slack, too.
**Riccardo Magliocchetti** 10:02 Yep.
**Aaron Abbott** 10:03 Yeah.
**Tammy Baylis** 10:04 Okay.
I haven't checked Slack this morning, Was the consensus to, reopen this in the other repo, or was it a different, Conclusion so far.
**Riccardo Magliocchetti** 10:24 Adjustment to the… to the reporter that we moved, development to the Python Genera repo, and they're all linked to the Slack channel, so…
**Tammy Baylis** 10:37 Okay, thank you.
**Riccardo Magliocchetti** 10:41 So I can handle that.
**Tammy Baylis** 10:43 Thank you.
Oh, 10… 10 after, I'm gonna stop sharing.
And, back to you, Riccardo.
**Riccardo Magliocchetti** 11:01 Outstanding?
What I'm working on this week?
I just added that today is started testing a bit more the Kali config stuff.
And… Yeah, like, reported an issue, and we have, Another contributor working on a fix.
So nice. And onto the core topics. Diego, you're the first one.
**Diego Hurtado** 11:35 Rai, thank you.
There is a comment there, I was taking a look at this, issue, I noticed that… There was a comment that said that we will bring this to the… the next meeting, so before I… I just found it and added it here. To be honest, I… Don't remember that well, the context here.
I think Lukas commented here as well. Sorry, I'm not feeling that well today.
So… just, I'm pretty much doing due diligence and bring it… Bringing it here to the SIG, in case there's something… We gotta discuss.
**Aaron Abbott** 12:44 Is… was somebody, like, working… working on it? Was it… I'm just wondering why this one came up again, just, you wanna… wanna close it out as duplicate?
**Diego Hurtado** 12:57 Right, the reason why is because, I use cloud to review all our open issues, and… It detected this as a candidate to be closed.
Because it's a duplicate, so… So yeah, I think Lukas commented as well, maybe we can close it as a duplicate.
In any case, I… I will… I added a comment there.
Explaining what, cloud, thinks about this particular issue.
**Aaron Abbott** 13:37 Yeah. No, that sounds good to me.
maybe we could just close it, and then if there's extra context in this one over the other one, we can copy it through. I can… I can do that.
**Diego Hurtado** 13:50 Right, I think you are.
**Aaron Abbott** 13:52 Cool. Thank you.
**Riccardo Magliocchetti** 14:08 Okay, next topic is also from you, Diego, and brought above HTTP exporter performance.
**Diego Hurtado** 14:14 Yeah… Can I share it, please?
Thank you. So… I believe, a while ago, I… Do you guys see my screen?
**Riccardo Magliocchetti** 14:36 Yes.
**Diego Hurtado** 14:37 Alright, great, I think I mentioned… this, effort we're doing at Dash Zero.
making… the protocol of… Exporters, not use Protob by implementing Protob ourselves.
No, that's, something that they also do in Java for the exact same reason, because, you know, you want to avoid A dependency on the dependency conflict stat.
Come along with that.
So, I think I also mentioned… That I thought using Rust would be a good idea.
And, well, it's mostly motivated by… what I… considered to be bad performance from this, pure Python implementation?
Need some more testing.
And, no.
If we consider just, the… encoding.
of, messages.
Pytopardof is actually… Pretty slow.
40 to 50.
Time slower.
But, when you consider the… Entire path.
That comes with, not only doing coding, but also exporting and so on.
It's not that slow.
It's only… 1.3.
That's that two times.
slow as the protocol of implementation, which I think is not that bad.
And, in my opinion, this, It's, enough, justification to… Not, follow… not to try and implement this in Rust for this particular case, I'm not… This doesn't mean that ain't… other uses of Rust are valid or not. I'm just talking about this particular case.
So… I wanted to show you these results, so… right now, I have this in a… in a dash zero PR, but I can… Open up.
An issue.
I'll share these results there.
Before I do that, I would like to know if, Someone has, any comments or questions?
Regarding this whole idea of, removing… Sorry.
Creating a new exporter so that we can avoid the protot dependencies.
**Aaron Abbott** 17:52 Yeah, I was just gonna raise again that we have… we have an open PR now for the… OTLP JSON exporter, which does remove the protobuck dependency.
I think, I remember we chatted about this maybe, like, 3 weeks, 4 weeks ago.
And I don't remember why the JSON was considered not acceptable. I think maybe the… It was a specific issue with one of the downstream tools, didn't support the JSON exporter, and then there was some question about Whether or not, whether or not the collector can automatically disambiguate between the two, or listen on the same port, something like that. But, I mean, that would be my preference, because it solves a lot of other issues for people.
Rather than doing this pure Python thing.
Yeah, and then the… yeah, I'll stop there. Go ahead, Dio.
**Diego Hurtado** 18:44 Oh, sorry, no, no, I didn't mean to interrupt. Is there something else you want to share?
**Aaron Abbott** 18:51 Well, yeah, the other thing I was gonna mention was, I think.
I think it was Buff. They just released, literally, like, 2 weeks ago, a… Python, protobuf, and gRPC implementation, and… It has, like, support for… falling back to a pure Python implementation if you don't have the native extension installed. So, rather than if we did want to go that path, I would kind of think that's a good way to do it, because we can avoid the maintenance burden of the actual protobuf implementation. I can try to link that blog post here.
**Diego Hurtado** 19:29 Right, thank you, I didn't know… About that, I'll take a look.
Okay, so the… the JSON implementation, And the… pure Python… Non-protob implementation.
are not against each other. We can have both, in fact.
I, I have been… Trying to get, lukas PR.
That implements the JSON exporter.
First, that's something I want to happen.
I want us to, have both things, the JSON exporter, And this… this as well.
The… the JSO exporter, I think has a downside, because the… It produces more bytes, because the encoding is not that, compact?
Spurdov.
So… That's an inherent downside of exporting JSON, right?
In any case, whether we use, oh, by the way, I do agree with you, Aaron, when you say that… us having to maintain our own protocol of implementation is a downside. I mean, it would be ideal if we don't have to.
I'll take a look at this, this study just mentioned.
But besides that, I would like to know if anyone has, like, any strong opinions, strong objections about going this way.
And with this way, I mean.
Using something else, to avoid having this protobuf dependency.
**Aaron Abbott** 21:32 Riccardo, you got your hand up.
**Riccardo Magliocchetti** 21:34 Yeah, like, you have a comment regarding the… your proposal of… like, using just the HTTP JSON exporter, but I think the issue would be, like… but, like, unless you use the Guardi config or you configure it yourself, but our defaults… Should be H2E protobuaff.
And at the moment, we don't even expect that.
But, yeah, so, like… like… I think that… you know.
Removing this possible conflict.
On use cases, like the injector, packaging, operator, and you name it.
Could be helpful, so… But, like, on the other hand, like, I have a question for Diego, like, do you plan to just, like, you would like to just propose another exporter for the same protocol?
Or… Remove the dependencies from the current one.
**Diego Hurtado** 22:45 I actually would like this proposal to take, This exporter to take the place of the… of the current… Hurtado exporter. The reason why… It's, it's something that you just mentioned.
the default, values, and also the fact that… The configuration file.
Right now.
Yeah, but 11th reconfiguration, right, doesn't?
Give that, Granularity.
So that, we… Someone can choose… By using the optometry configuration file, If they want A protot implementation, or a non-protob implementation?
So the only thing that they can choose is if they want to use HTTP Proto.
Which means that, in order for them to This is staying, this will have to take the place of the current.
Yeah,
**Riccardo Magliocchetti** 24:10 The name is already taken, like…
**Diego Hurtado** 24:12 Exactly. The other thing that I have been… sorry.
Taken care of, because, I… I made this new exporter, Follow the same… Naming, And import paths as the protocol one, so that… If, if they even… If they install this package.
And remove the other one.
it'll match.
Except for the fact that this one also doesn't use requests, so there's a little discrepancy there.
I, I think removing requests from… Our SDK is also a good thing, but that's another topic.
In any… in any case, There is an alternative to completely replace the protobuf implementation, By this one.
Which is… which is that one, right? That, we… we have two separate packages, but, The user decides which one to install, and they all behave the same.
Except for the requests, usage.
Now, yeah, that's also something… something we can do, if… I think, it adds complexity, and, adds, some… Something else for the user to… To be aware of, right? That there are two implementations?
But, but yeah, that's… that's the current state of things.
**Aaron Abbott** 26:20 Yeah, I just want to make sure that we're, like, solving the problems that users are having, so I hear you on the performance concerns and stuff like that. I just… I don't know if I've seen a lot of… like, like… The main thing that seems to be the user experience issues related to Protobuff, whether that's… that's gotten better, to be honest, but I understand for Injector and for the operator.
it's still not great to have to guess ahead of time what the AVI is gonna be. So I think, from my perspective, that's, like, the main problem to solve, and I think we should wait and see how people respond to the JSON exporter before we take this path, just because Like, I think… Lukas, you got your hand raised too, but I think that one solves… I just want to make sure we're focusing on the issues that users need to solve.
Before we make a complicated solution.
Yep, Lukas, you wanna go ahead.
**Lukas Hering** 27:22 Yeah, I just want to say one more thing, like, this might be pretty radical, but I think, our, Alex Bowen, he posted a C++ wrapped Python SDK.
I feel like if you want, like, really safe, injection capability? Like, with the injector, like… if you just, you know, take the C++ SDK and then just ship that as an entire SDK implementation, that would solve everything, like, almost instantly.
So, maybe, like… Because it seems like this is really mostly an issue for the injector and operator, if I'm not mistaken. So, like, maybe… For that particular case, you just wrap this C++ SDK.
**Diego Hurtado** 28:15 Right, yeah, that's, another possibility. I've discussed this with Alex as well.
There is, at least in my… the depression that I have is that that's still a little… a little bit… A way to go.
Not, only because, the… the SDK… And exporters are… Some separate things, right?
In the sense that… In Python, we separate them and incorporate them dynamically by using entry points.
So that'll mean it'll be necessary to… compile an SDK… with the… Exporters that you want to use?
So, it's not that straightforward, right? At least, there is, still some… At least in my opinion, right? I don't know if Alex feels the same, but at least in my opinion, I think the… There's still a little bit of… thinking, working on how this is gonna work, right, so…
**Lukas Hering** 29:47 Yep.
**Diego Hurtado** 29:48 This is a much more immediate solution, in my opinion, as well.
**Lukas Hering** 29:52 Yeah, I was just, like, I mean, thinking further downstream, like, I'm assuming you'd also want to have a gRPC one, right? And implementing that… without the gRPCIO dependency.
**Diego Hurtado** 30:06 We are also doing that. In fact, we already have a… a pure Python gRPC implementation as well, that's you.
**Lukas Hering** 30:18 Okay. Yeah, I think… Yeah, I don't… yeah, I think I agree with Aaron, though, like, maybe it's worth waiting a bit, but, like, if we did really want to commit down that route, we probably would want to have A… an ability to… Either through, like, an optional extra to turn on, like.
Some sort of use of native code.
Just so that the performance… Isn't noticeable, the performance degradation?
I know that, like, in aggregate, it's not… horrible, but, I mean, there's definitely probably use cases, or… Certain users that would notice the impact if we were to just start switching to this.
So…
**Diego Hurtado** 31:04 Right, no… There is a possibility… That we can consider, right, No, actually… I don't.
Sorry, because I haven't, actually considered the fact that request is also a dependency, yeah, so… M… So… What do you think, should we do? Should I… Open an issue… And a PR, so we can discuss it there. I guess, we have taken… a good chunk of time of this SIG meeting.
**Aaron Abbott** 31:53 I think issue is good. I don't know if we're ready for a PR. It sounds like there's, like, a couple…
**Diego Hurtado** 31:58 No, I meant, sorry, I mean a rough PR so that you can… Oh, sure. Have the issue and understand implementation as well.
**Aaron Abbott** 32:08 Yeah, sounds good. And Diego, if you don't mind, like, the… some of the trade-offs and alternatives we discussed, if you could just add them to the issue so we can Or, like, the, you know, pro-cons for each approach, it would be helpful to see it all written down, I think.
**Diego Hurtado** 32:24 Alright, I'll work on that, I'll open an issue. Thank you all for your input.
**Riccardo Magliocchetti** 32:30 I think we have already an issue, I'm adding it to the… With the notes.
**Diego Hurtado** 32:37 Alright, makes sense.
Thank you, Riccardo.
**Riccardo Magliocchetti** 32:47 Thank you… Can I… okay, thanks.
Sure, Kevin?
**Diego Hurtado** 33:04 Am I still sharing?
**Riccardo Magliocchetti** 33:06 Yeah, yeah, thanks.
Okay, next topic is for log stabilization.
From Radhika?
**Radhika Gupta** 33:17 Alright, thank you. So I was just wondering, like, what is the, current status on water stabilization? I know we had this conversation, like.
**Lukas Hering** 33:26 You're, like, a really quiet… sorry, I don't know if anyone else.
**Radhika Gupta** 33:29 Can you hear me now?
**Aaron Abbott** 33:33 It's still pretty quiet for me, too.
**Diego Hurtado** 33:35 Yeah, same here.
**Radhika Gupta** 33:48 Oh, can you hear me better?
**Diego Hurtado** 33:51 Yep, which one are we at?
**Radhika Gupta** 33:52 Okay, yeah, so about lock stabilization, I know we had this conversation, like, a few SIGs back, so I was wondering, like, if there are any outstanding tasks that we need to, like, go through, I can help out with that.
So just wondering what was the current, like, status on this?
**Riccardo Magliocchetti** 34:16 Thanks, I added to the notes this, issue.
I'm not sure it's the only one, because I remember… Let me check.
because I remember Diego APR adding, The enable method to the logger and the log processor.
We were linked from an issue from Ludmil, I think.
But, yeah, so the long delay is that, yeah, we have some… still… still some issues open.
But, yeah… I don't remember details… the details about that.
**Liudmila Molkova** 34:58 And the one, the big one, was the enabled.
And I think Diego has a PR for it, I didn't have a chance to take a look.
**Riccardo Magliocchetti** 35:12 Yeah, I should be like this one.
So yeah, my suggestion would be, like, please take a look at the open issue here.
And see if anyone… It's still missing a PR.
Otherwise… Helping with the reviews would be appreciated as well.
**Radhika Gupta** 35:32 Yeah, sounds good, thank you so much.
**Riccardo Magliocchetti** 35:35 Thank you.
Last topic for today, Lukas?
Yeah, the incubating attributes.
**Lukas Hering** 35:50 Yeah, I, I opened this PR because currently.
Due to the introduction of the, self-observability metrics.
we've introduced a dependency on, like, semconf the private incubating Namespace?
in… Basically, all the exporters now.
I know that… Riccardo and… I think, I forgot who else looked at this, but I guess there was questions? Oh yeah, There's questions on… why this is needed? And I guess maybe it's just a misunderstanding from me, but the understanding that I had under, with the incubating SEMCOM is that in between minor versions, there can be breaking changes.
And in our exporters, we have, like, loose requirements to allow for newer versions of the SDK to be used with each exported version.
So that would… so in doing that, it would kind of violate that. So I'm not sure if other people agree with me on this. The solution that I have in this PR is to just inline everything, like, bring… bring all the… Attributes we need in, and that way, we don't… There's no… there's no risk of breakage.
And then once those attributes do become stable, then we can remove the, the vendor definitions.
**Liudmila Molkova** 37:38 Yeah, this seems like a great option, because even though we don't really make breaking changes.
de facto in incubating parts, because SimConf tried to deprecate instead of remove, and still it's incubating, right? And depending on something incubating from a stable component, It's not good, and it's very cheap to just inline constant names.
And I think this is what Java recommends, and what Java does as well, and from some conf perspective, I hope, I think, I hope we have it documented somewhere that Dant instrumentations, should applications can depend on incubating some kind of instrumentations probably shouldn't.
instrumentations that we have in contrary part, kind of way, because it's the same ecosystem, and we have versions pinned, so, like… It's okay for there.
**Riccardo Magliocchetti** 38:56 like, I don't have strong opinions, and I remember asking the question, like, why we want to do this.
But, yeah, like… It's fine, like, like… like, maybe, like, we can wait a bit more and try to stabilize the names, at least, so… like, because, like, we can work also on the semantic convention side to have this out of… Incubation.
But yeah, like, I, like… For me, it's fine.
**Lukas Hering** 39:34 I mean, I'm fine leaving it as long as, like, I guess if we can just guarantee that nothing will ever break in the incubating, namespace.
**Riccardo Magliocchetti** 39:45 That's a kinda strong guarantee, like…
**Lukas Hering** 39:50 Yeah, I'm just saying, like, yeah, from a… from a,
**Riccardo Magliocchetti** 39:53 Yeah.
**Lukas Hering** 39:54 technicality perspective, like, yeah, like, this.
**Riccardo Magliocchetti** 39:58 I mean, like…
**Lukas Hering** 39:58 Need to do.
**Riccardo Magliocchetti** 40:00 Like, it happened in the past, already, but… Yeah, like, you should not happen.
Hopefully, anymore, but…
**Liudmila Molkova** 40:12 So the… well, the way to guarantee it would be to, have a test.
Was the oldest version for the exporters, was the oldest version of semantic conventions Artifact.
Britain never, pretty much never bumped this version.
**Lukas Hering** 40:39 Right.
Or are we… I think we need to actually test, like, an old… yeah, it gets a little confusing. Like, we have to test… this has already been in place for a while, so we have to probably test, like, older version of this exporter or whatever, but… I figure, like, we can just fix it now, and then not have to worry about it.
**Liudmila Molkova** 41:04 Yeah, why wouldn't do this, Riccardo? Why would we, keep the dependency that we don't need? Dependencies suck.
They have other side effects.
**Riccardo Magliocchetti** 41:23 Well, the appendices are great. Don't say that.
**Liudmila Molkova** 41:29 It's like, we can remove a dependency. Let's just do it.
**Riccardo Magliocchetti** 41:37 Good.
Anyone else has opinions?
like, but anyway, the… Liudmila suggestion to… to start testing with the older SDK… SDKs, the… It's a good one, because we had already, again, a regression on that front.
with exporter, we're acquiring new stuff, added to newer SDKs, so we broke.
**Liudmila Molkova** 42:08 I'm proposing to drop the dependency, to be fair.
If there is a strong desire to keep the dependency, then we should test the… Oldest version.
Of some conf in the… in exporters, but it just complicates things for no good reason, I feel.
**Riccardo Magliocchetti** 42:38 Yeah, let me add it to the notes.
**Lukas Hering** 43:44 I guess one correction, it wouldn't technically be the oldest… it's just the oldest SDK that introduced those metrics.
**Riccardo Magliocchetti** 44:24 So, like, maybe we can discuss this a bit more offline, or… On the PR.
But, like, again, for me, it would be fine to merge the PR.
But, like, maybe, like, Give me a bit of time to understand if you can try to… Stabilize the… the metrics as well, so maybe, like, we can avoid… Nothing.
Thanks.
Okay, we have… Still 15 minutes?
More comments? Topics?
No? Okay, so you have 15 minutes back. Thanks, everyone.
See you.
**Aaron Abbott** 45:14 Alright, see y'all later. Bye.
