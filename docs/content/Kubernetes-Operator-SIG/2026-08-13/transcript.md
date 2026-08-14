SIG: Kubernetes Operator SIG
Date: 2026-08-13
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

Pavol Loffay (Red Hat LLC) 00:05:04 Hello, hi everyone.
Ilia Petrov 00:05:09 Hello.
Pavol Loffay (Red Hat LLC) 00:05:10 Can you hear me?
Ilia Petrov 00:05:13 Yes, sir.
Pavol Loffay (Red Hat LLC) 00:05:14 Awesome.
Mikołaj Świątek 00:05:34 Hello.
Jacob, are you typing and not talking for some specific reason?
Jacob 00:06:20 No, I just, wanted to type. Sometimes I want to… I like typing in the chat, I don't know.
Usually I do it when I don't want to start full discussion on a thing, and I just want to, like, say a little quip.
Mikołaj Świątek 00:06:37 You can, you can try to, try to fight the tendency to overcome it.
It's… there's two problems with it, and the fact that the comments are too long is a smaller one of them. The bigger problem is that just an overall LLM failure mode is that they try to spill context on whatever they're doing.
Jacob 00:06:57 Yeah.
Mikołaj Świątek 00:06:58 It results in comments which are just completely with negative value, like, for example, you tell it to do something different, and then it makes comments about that in the comment in the code, which is just… Nope.
Completely irrelevant, in fact, completely irrelevant information, actively confusing.
Right? Yeah. But it just does it because it's at the front of its context.
Yup.
Anyway, I think we can get started.
I am actually going to… Do you guys have anything that you haven't put in the agenda? Right now, there's only one… my item inside of it.
Jacob 00:07:41 I don't think I have anything. I feel like it's been relatively quiet. I was wondering if we could get your, injector PR, up and running.
Mikołaj Świątek 00:07:55 That's a POC. You can take it and do whatever you want with it. It's a POC. Yeah, I don't intend to merge it as is, like, the open question of architecture support.
It's still there. Why don't I… Okay, the screen-sharing UI for Zoom on Linux is confusing me, but now I figured it out. Can you see this?
Jacob 00:08:20 Nope.
Mikołaj Świątek 00:08:22 Okay, so… there's one item from me, and I'm just asking for a review.
This is plus one 1400 lines.
But it's just tests.
Jacob 00:08:36 Yeah, it's pretty uncontroversial. I was reading it, before you… before you joined.
Mikołaj Świątek 00:08:42 Yeah, it's really just… it's a bunch of machinery for the end-to-end tests, which I also plan. I have a follow-up ready, which is going to part our… current chainsaw instrumentation tests into this machinery, because they're way smaller of it, it's way easier to express, like, repetitive parsing logic in it. And this is a test which does, like.
It installs Prometheus Operator and a Prometheus, it has a service monitor, and then a scrape config, a raw scrape config.
which point to, like, Node Exporter running in there, which I haven't chosen Node Exporter because it builds for all the… again, it has builds for all the architectures that we support.
And then it just ingests… scrapes that same set of metrics in two ways. One directly through Prometheus, and the second one through an auto collector and a target allocator, which also export to the same Prometheus via the, like, OTLP endpoint with no translate enabled.
And then you just compare both of those inside Prometheus itself.
And check if the labels are the same. And that's it. Like, this is the first test we have that actually does this, like, end-to-end.
Well, and it's, and it's, it's like… I don't know why GitHub is being so… insanely slow.
Jacob 00:10:08 There's a,
Mikołaj Świątek 00:10:09 Is it an outage?
Jacob 00:10:11 There's an outage. Yep.
Mikołaj Świątek 00:10:12 Yeah.
Jacob 00:10:12 It says it's resolved, but I don't think it is.
Mikołaj Świątek 00:10:15 I mean, it might be resolved from their perspective, it's just they have a backlog, but that's.
Jacob 00:10:20 Yeah.
Mikołaj Świątek 00:10:20 this… this succeeds. It doesn't add, like, any dependencies that we don't have yet, and it's overall, I would say, pretty straightforward, what these tests do.
And it's just a bunch of code, mostly because we're doing stuff like adding this, like, PROMQL, Parsing stuff, and… And tests for the PromQL parsing stuff.
And that's, like, the majority of this pull request.
And also some, like, just YAML manifests for the stuff that it's doing.
Jacob 00:10:56 It's… it's pretty neat how you can, do declarative in fit, like, you know, actually have this configuration as code here. It's… it's pretty nice.
Mikołaj Świątek 00:11:06 Which part do you mean, exactly?
Jacob 00:11:09 Like, being able to just… Create the… Create the service monitors and the code, and then also do this verification of the metric names and stuff.
That's nice.
Mikołaj Świątek 00:11:25 Yeah, I'm surprised that this is as simple as it is, because this was, like, conceptualized by an LLM.
Yeah. And I was surprised at how simple it ended up being.
So yeah, that's the one thing I had.
Feature gates… I… I don't think anything changes, there's still the… This is in beta. I think eventually it might go… it should go to stable.
Jacob 00:11:58 Yeah.
Mikołaj Świątek 00:12:00 This one is going to disappear very soon, I say it every time, but very soon it's almost there, because I have, like, a pull requests open in my fork that removes it, and instead it just does… makes it a configuration option.
On the strategy?
And it's a pull… it's a pull request that, like, implements plumbing to make strategies configurable.
At all. I have, like, a series of 5 stacked pull requests that progressively implement more stuff on top of that, and I just haven't gotten to.
Submitting them yet, but… This is… This is gonna go away. I don't know about these, those are Pavols, so he can, he can, give his opinion. I think this one should also go to stable. It's just that the, Contributor who was handling it, didn't finish it.
But it's enabled by default.
Any, like, comments?
Jacob 00:13:05 Zip.
We've had a lot more bridge PRs recently, I don't know if you've noticed that.
Mikołaj Świątek 00:13:11 I have, because I… I look at all the PRs that are open.
I think Bridge… I think there are users of Bridge, finally.
Jacob 00:13:20 I know, I'm surprised, to be honest. I… there's… I need to, at some point, talk to the other op-amp people about, like.
I don't know, Andy and I had these plans a while ago, before they got acquired by Dynatrace, about, like, merging in what the bridge does and what the supervisor does.
And I'd like to… I don't know, pick that up again, but I am reviewing these PRs as well. I'm gonna review this one that just came in,
Mikołaj Świątek 00:13:52 Do we have an issue for… for these Golang flag… for these Golang flags feature gates?
Jacob 00:13:58 I don't think so.
Oh, great, now GitHub isn't loading for me.
That's awesome.
Mikołaj Świątek 00:14:10 I'm gonna check who is… it's loading for me, so I have, like, Eastern European privilege or something.
Jacob 00:14:16 Exactly.
Mikołaj Świątek 00:14:16 Over here.
Jacob 00:14:17 I think that there's a US West outage or something. I mean, I'm on USS1 for sure, but, out my, like, company's, GitHub runner, provider, They said that their data center's water cooling failed, and it sounds like the entire data center melted.
Mikołaj Świątek 00:14:36 Oh, nice.
Jacob, I'm just pointing it… I'm just pointing out who is the offer of adding this.
Jacob 00:14:42 Yes, okay, okay, I can do it right now.
Mikołaj Świątek 00:14:47 You can also just file an issue, so we don't forget.
Jacob 00:14:52 No, I'll just do it right now, it's fine.
Mikołaj Świątek 00:14:55 But then you'll have to remember to delete this after the next release.
Jacob 00:14:59 That's fun.
Mikołaj Świątek 00:15:01 So this is what we got, and there are some issues that I actually put in here.
One is this, because I… I don't remember, I don't understand, so… There's this… this contributor here wants to fix a problem where if it's the default version, that something's wrong with labels and status and whatever, and… I am looking at this, I'm asking myself, why do we not Because for instrumentation.
When you don't put in the image, we just put the default in there.
There's a defaulter that sets the default image, and after the actual CR is created in the cluster, it actually has the image set.
Why isn't this the case for the collector?
It would fix this problem, and probably many similar problems.
Does… do you guys know why? Why is this?
Jacob 00:16:01 I'm reading through this… Wait, can you go down to your comments again?
Mikołaj Świątek 00:16:09 The comment where I asked the question is here, basically.
Jacob 00:16:13 I don't want to see the imaging.
Mikołaj Świątek 00:16:16 Why don't we just set the image?
Jacob 00:16:21 I think what this is, like, similar to what the thing we're trying to do for instrumentation is, where we're trying to avoid setting default images now, no?
Mikołaj Świątek 00:16:29 But we are doing it, it's just.
Jacob 00:16:31 We are doing it right now.
Mikołaj Świątek 00:16:32 brother.
Jacob 00:16:33 epidemic.
Mikołaj Świątek 00:16:33 explicit, like, and if it was explicit, it would… let us avoid a bunch of, like, special cases in the code, like what is… what is attempted to be added here, where it's like, oh, if the image is not set, then we do a bunch of, like, special casing in all sorts.
Jacob 00:16:49 Oh, I don't like that at all.
Mikołaj Świątek 00:16:51 I don't like that either, and I think the solution to it is… because you… look, you have.
Pavol Loffay (Red Hat LLC) 00:16:56 This shape.
Mikołaj Świątek 00:16:56 label, and this label is apparently confusing. I agree with you.
Pavol Loffay (Red Hat LLC) 00:17:00 It's confusing.
Mikołaj Świątek 00:17:00 choosing.
Jacob 00:17:02 I don't think it's confusing. I think that that's the label that you get when you do nothing. I think that the answer is do something.
Mikołaj Świątek 00:17:08 I mean, yeah, but, like, this is useless. Latest what?
It should be the actual version that is running.
And we do know.
Jacob 00:17:16 Where do we…
Mikołaj Świątek 00:17:17 It is.
Jacob 00:17:18 Where do we set that right now?
Mikołaj Świątek 00:17:20 somewhere in the manifest, labels here. The problem is generally that, like.
Jacob 00:17:26 This… I guess what I'm saying is, like, this feels like, The way that they're solving this is incorrect, and we should instead Yeah, Pavol, we can hear you. Do you have a thought?
Mikołaj Świątek 00:17:43 But, no, I can't hear you.
Jacob 00:17:45 I heard Pavol for a second earlier, but no, no more.
Pavol Loffay (Red Hat LLC) 00:17:54 And now? Is it working immediately?
Mikołaj Świątek 00:17:56 it's good.
Pavol Loffay (Red Hat LLC) 00:17:58 Okay, Yeah, I think it's the anti-pattern to default. I think we had more issues with setting the defaults than leaving it blank, so I don't know what is the issue, actually.
If you could maybe… Go back to the description.
Mikołaj Świątek 00:18:22 Yes, so the default collector image.
But the problem is that we have, like, these manifest generators, which, for example, add labels, like, version.
And those don't handle the empty image correctly.
So, instead, if you use the default, like, you don't set anything, and we, by default, have version, you know, 0.156.0, let's say, right?
You don't get that on the label. You get latest.
The latest is useless.
Sending…
Pavol Loffay (Red Hat LLC) 00:19:02 I have…
Mikołaj Świątek 00:19:02 Yeah, they have.
Pavol Loffay (Red Hat LLC) 00:19:03 These label generations should be probably fixed, no.
than safe.
Mikołaj Świątek 00:19:07 Yes.
Pavol Loffay (Red Hat LLC) 00:19:07 bridge.
Mikołaj Świątek 00:19:09 Yeah, but this… and they are doing it here, essentially, just as the fix, right? The fix is something like this. If the image is empty, take the image from the configuration, but this feels… this feels like, like, patching a… some kind of more fundamental problem, like this.
Jacob 00:19:25 Yeah, I agree. I think that we should just not… I don't think we should do this, and I think we should just tell the user that they should set the image. I think that, like.
We should be more in the habit of requiring people to set an image than… Us defaulting the image.
Mikołaj Świątek 00:19:44 Agreed, Rodley.
Jacob 00:19:47 It just goes into the challenges that we have with, like, upgrades.
the more burden that we have there. I think it's fine for us to, like.
Bump the default and do that on behalf of users.
Certainly when we have that information, but I think that doing it in this case is, more fraught. I think if we wanted to do it, doing it the way that you said, where it's in the… A hook, where if it's not set there, then we change it as a better option.
But I think doing it this way, where we're changing all the manifest generation, is definitely a hack.
Mikołaj Świątek 00:20:27 So, like, to me, the question is, okay, so do we accept the hack right now and just declare the intent that when the collector is stable, we're going to require the image to be set when we go from Beta 1 to Beta 2, let's say?
We could do a braking change like that, right?
Pavol Loffay (Red Hat LLC) 00:20:47 So far, our philosophy was the operator was kind of… Tightly coupled with a collector version.
And therefore, it made sense that the operator was setting the collector.
Right, because if you look at how we operate, we as well release… we release Operator per collector release. So, a specific version of Operator We guarantee that it's compatible with a specific version of the collector.
Mikołaj Świątek 00:21:18 Yes.
Pavol Loffay (Red Hat LLC) 00:21:19 And so, if we start requiring users to set the image, I'm the true… If… If there is… a goods… if this align with that philosophy, right? Maybe then we can say, okay, we want to decouple from the collector releases altogether.
Whichever trade that we want.
Mikołaj Świątek 00:21:44 We might want to once it's more stable.
We've had some questions for… we've had some requests for rollbacks, for example, and the reason we said no to rollback was because of this, like, tightly coupled… compatibility.
requirement, essentially.
I've… So, what I'm getting from this is that… We're not aligned.
So we should open an issue and have a discussion about this. And in the meantime, what this contributor wants to do is probably correct.
like, it's a hack, but it's a hack that's in line with how the application works right now, and I don't think there's, like, any nicer way of doing it. I do think that… Why is this even being changed exactly? I'll have to actually review this, but, like, conceptually… Conceptually, what should happen is that, like, if we're adding… app.kubernetesio.version, then it should be the actual version that's running, and not latest. I think we agree with that, right?
Jacob 00:23:06 Yeah, I just think that the mechanism for doing it, the way that this person's doing it, is, opens us up to more hacks, and I'd rather we, for now, just, like, default the image In the webhook, rather than doing this.
Mikołaj Świątek 00:23:21 What is the negative of… what are the downsides of defaulting?
Jacob 00:23:26 Of this.
Mikołaj Świątek 00:23:26 in the webhook, and defaulting the image in the webhook, what are the.
Jacob 00:23:31 I mean, it just kind of is the same as what we have today, no? Where… I think what happens right now when we don't set it is… Like, I need to look at the code for… let me open this up.
Maybe there's, investigation audits.
Pavol Loffay (Red Hat LLC) 00:23:45 on the upgrade.
Jacob 00:23:46 Joe.
Pavol Loffay (Red Hat LLC) 00:23:47 I'm not sure if the upgrade would then work if the image is set.
Jacob 00:23:54 Yeah, actually, here it is. If you go to,
Mikołaj Świątek 00:23:57 It works for instrumentation, so it can work the exact same way.
Jacob 00:24:01 Yeah, I agree. I can show you right now, Mikola. Can I do the share?
So… Can we see my screen?
Yes.
Okay. We just do it right here, where if the image is nothing, then we set it here.
Which, we could probably do in a better way. It looks like Antoine made this change.
But it's probably from a refactor.
I mean, do the… get blamed on this.
Which one is that?
There it is.
This was in Remove All Getters. What PR is this?
Yeah, so it wasn't really much of a change.
I assume that we've had this for a long time, and what we could probably do is just add it into the default webhook and remove it here, and then just error if image isn't set at this point.
And I think that that would probably be a better approach, and then later, the breaking change would be removing it from the defaulting webhook.
The only… the thing… the only case where this would break somebody is if they're using the operator without the webhooks.
In which case, I would argue that they should be setting the image anyway, if they're already not using the webhooks. They should be more careful about, breaking changes, because the webhooks are where we would handle upgrades for them.
Which is why, like, I think that it makes more sense to do it there.
Mikołaj Świątek 00:25:57 I'd be in favor of changing it this way, but I'm not, like, fully… I'm gonna try fully… I'm gonna fully, like… conceptualize the consequences.
Ugh, I'm doing it.
Jacob 00:26:13 I think that that would be it. I think it would really only break people on the default webhook, and we would error the… or who aren't using the defaulting webhook.
And we would error, hard, rather than today, where we do it, on their behalf.
But I think that the… the slice of people that are not using the defaulting webhook and not using their own image is probably relatively small, in my mind.
Mikołaj Świątek 00:26:42 The other question is, like, what do other operators do about this?
Jacob 00:26:47 I feel like I remember looking up Prometheus Operator.
Mikołaj Świątek 00:26:51 Prometheus, I think, keeps… keeps it empty. I'm not… I don't think the webhook adds anything.
Because for instrumentation, there is, like, I think a good reason to do it differently, and that reason is essentially that… Like, instrumentation is kind of like an ob… is kind of like a record for injection to happen.
Asynchronously, so…
Jacob 00:27:20 Yeah.
Mikołaj Świątek 00:27:20 having, like, an explicit point where it's changed, because if instrumentation worked this way, then just doing the Operator upgrade in the background would cause you to have something else suddenly, whereas when we… if you explicitly change what's in the CR, then you have a point in time where you can see.
That, yes, it changed right now, and from this point on, we, you know, we're injecting a new version.
Jacob 00:27:43 image path cadence.
Let's see… it looks like this is what they do.
Which is actually kind of similar to what we do.
Mikołaj Świątek 00:27:57 Yeah, the only question is… so something… maybe that's an argument for keeping it, okay?
Jacob 00:28:03 I don't know, I kind of want to diverge from them in this case, like, I'd rather that we do it in the defaulting webhook.
Return spec image if image contains a tag, otherwise return image.
What are this diversions?
For the container labels.
That'd be a step above. So this is McDon set.
With labels. Object meta, Get labels.
Where's object meta, get object meta… This is P. Prometheus Agent.
Oh, it's literally the object meta, they don't do anything special there.
Mikołaj Świątek 00:28:51 Maybe they just don't put this as a label on the thing.
Jacob 00:28:55 Yeah, I mean, that's… let's see.
with labels config.labels, and where is config? From config.
Mikołaj Świątek 00:29:03 So they also have…
Jacob 00:29:05 a good thing.
Mikołaj Świątek 00:29:06 So they… what probably happens is that they have, like, a set of labels they specifically add, not from the CR, but from the global config as well.
Jacob 00:29:16 Yeah.
Mikołaj Świątek 00:29:17 Maybe we should do something similar in that case?
Jacob 00:29:20 I guess we could do that, if nothing else is set. I mean, it's not the end of the world. I think I'd still rather would see us just add… move this to defaulting webhook, and then it would… it would just work.
But… I understand the trepidation there. Also, this is my change. Do you like my change?
Mikołaj Świątek 00:29:40 It's beautiful.
Jacob 00:29:42 Thank you. It took a long time, so it's…
Mikołaj Świątek 00:29:45 I can see that many tokens were spent on the implementation of this, yeah.
Jacob 00:29:52 Yeah, you can tell, right? Yeah, exactly.
Mikołaj Świątek 00:29:55 Excellent.
Jacob 00:29:57 And this, for the 2 version, I set it to 160, which is in, like, 3 versions or something.
Mikołaj Świątek 00:30:01 Yeah, it's okay. It could literally be the next one, I don't care. I don't think anyone cares about this specifically.
The only question for me is what to do about this pull request. Do we accept this pull request? Do we conceptually accept this pull request, but don't like the implementation? Or do we reject the pull request and say, no, we're going to the defaulting thing? I don't want to… because it is a legitimate fix.
So I don't want to hold it up with our… I know.
Jacob 00:30:34 portables.
Mikołaj Świątek 00:30:35 Without, without bike shedding, about,
Jacob 00:30:38 Yeah.
Mikołaj Świątek 00:30:38 Well, it's not bike shedding, that's a joke, right? But with our, internal disagreement about how to do this.
So, I'm, like, I'm okay with what the… with what the contributor did there, personally, like, I'm alright.
maybe there's a nicer way to do it, if you… but I think we should accept a change like this.
Because right now, right now, the… some of the stuff we do is just incorrect. And, like, if… if it can be made correct, even if a way that's not nice, then I'd rather do that than wait for the… more foundational.
to come about.
Jacob 00:31:21 Yup.
I think we should… I think, conceptually, this is okay. I think I would rather them just move it to the webhook, so that we can later remove this functionality.
Mikołaj Świątek 00:31:35 I also think that maybe, maybe this should be refactored to work in a way that is, like, more similar to what Prometheus Operator does, where…
Jacob 00:31:46 I actually don't like what they do in this case. We… our setup used to be like this, and we moved… away from it, so that it would be a little bit more… it was more easily testable. The problem with their setup is that they do a lot of, like, global changes, and it actually makes, like, reasoning through their code very frustrating.
That's fair enough. I think that our code is, like, actually pretty, for the manifest generation, I'm happy with how it is, because it's easy to reason about, and easy to test.
Which I, which I do like.
Mikołaj Świątek 00:32:23 So, but in that case, what the contributor is correct, I think.
Because what they did is, essentially, when you build the manifest, you set the default in the CR.
Jacob 00:32:38 Yes, I think we would move it to the default, and then the manifest would build the way that it builds for everything else.
Mikołaj Świątek 00:32:44 I'm okay with that.
As long as it's, like, a single place where you said that there are not 50 places, where 50 places where you set it.
Jacob 00:32:50 Yeah, I just don't like that aspect of it right now.
This is super annoying.
Mikołaj Świątek 00:33:01 But, alright, I'm… I'm going to… I'm going to review this.
There's one thing that's confusing about their pull request, but I'll just, like… And I encourage you to review it as well.
Jacob.
It's tagged.
Jacob 00:33:21 young.
Mikołaj Świątek 00:33:22 That's what SIG right now.
Jacob 00:33:23 Yeah, yeah, I can, I can add review.
Mikołaj Świątek 00:33:28 Alright, and… There is… Two more things under Discussed SIG. Let me reshare, actually.
There we go.
This was this one, yeah?
Jacob 00:33:49 I'm going to drop briefly for a call, and I'll be right back.
Mikołaj Świątek 00:33:55 There's a pull request by Yuri.
And what Yuri wants to do is… Finally resolved the… Annotation and label problem.
But the problem is that we keep some of them, we don't always overwrite, right? We keep things that the user added out of band for annotations and for labels.
on resources.
And the side… this has various undesirable side effects. For example, an undesirable side effect is that if we add an annotation, then we can't delete it later.
There's a special case for the Prometheus annotations, for example, because you can set something on our CR which houses it to add the Prometheus scrape annotations on a collector, deployment slash daemon set slash stateful set.
But then, if you disable that option, it doesn't delete those annotations.
Because we cannot delete annotations. We don't know who added them.
And there's, like, a fix in there that's kind of like… Add a special annotation that tracks if we added it or not.
And then it works.
But here, what Yuri is doing is actually saying.
No, we don't preserve anything at all.
And then we just add settings to the operator configuration, where the user can set preserved labels and preserved annotations, which are… which we're not going to touch, but we're going to delete everything else on reconciliation.
And this is a braking change.
I wanted to solicit feedback about this. What do you think? Is this worth doing in a breaking way?
Benedikt Bongartz 00:35:49 at some point?
The question is when?
Mikołaj Świątek 00:35:55 I mean, we can do it right now if we want. It's not… we're not breaking anything in a… in reconciliation or in any of the custom resources. This is just an operator behavior that exists.
And it's.
Benedikt Bongartz 00:36:09 That's because it's explicit.
Mikołaj Świątek 00:36:11 It's nice because it's explicit.
like, the… I… I'm saying, I like… I like the end result of Yuri's change. I'm just not sure how… how, like, disruptive it's gonna be for people, and if it should actually… Well, it doesn't make sense to do, like, a feature gate, right? Because it's just a config option. It's equivalent to adding the config option that this pull request already adds.
And Pavol, you're a reviewer on this, so you won't be able to avoid it forever.
Pavol Loffay (Red Hat LLC) 00:37:01 I have to take a look. I have to take… I have to review it to more details.
Mikołaj Świątek 00:37:06 I mean, the logic itself is really simple. Like, the change is fine, in my opinion.
It's just… the question is, do we want to do it?
Do we actually want to do this?
And I'm not sure.
I can push it back for now and wait for Jacob to come back, because I also want to get his opinion, but… but yeah, essentially, this would solve the problem that we have at the cost of doing a braking change that is potentially somewhat disruptive. I don't know how disruptive.
Exactly.
But it would be disruptive.
there's a thing here, which I don't really think is super controversial, but I'm showing it off anyway because I want everyone to know that this is something that is happening. Like, we are… Adding the ability for a target allocator to export telemetry via LTLP, and this is already added to the actual target allocator application, this just adds it to the CRDs.
And I've enforced here that the structures that we're adding for this telemetry are consistent with declarative config. We can switch to full declarative config in the future.
If that's what we want, without doing breaking changes.
But right now, this is kind of all written by hand.
There's a test that checks that it's… With the creative conflict.
I… if you want to discuss this, I'm okay, I'm mostly showing it off, so that you're aware. Because this is, like, a pretty major… change to the CRDs, so I want to have, like, a second… maintain a review on it for Wimarks.
Pavol Loffay (Red Hat LLC) 00:39:02 I think we talked about it last time, and the conclusion was… this PR just adds a subset of the declarative config, if I'm not mistaken, and if later we… We want to introduce it as well for the instrumentation, and we can still… change the internal objects without breaking the CRT, if we kind of decide to kind of model it a different way.
So I think it's fine to go ahead with this PR.
Mikołaj Świątek 00:39:40 I think so as well. And I've since had… I asked the offer to add the test, so… and there's a test in here which essentially just marshals this to YAML, and then unmarshals it into the creative config and checks that it's valid.
So…
Pavol Loffay (Red Hat LLC) 00:40:01 Yeah, I think that's… That's really what we should be doing here.
Mikołaj Świątek 00:40:06 Yep.
Yeah, but essentially, I'm showing it off. I'm actually going to add both of you.
as a reviewer, scary, because, like I said, I am… I want to have a second maintainer review. You don't have to read… most of it is kind of… Like, it's, like, plus 2,000 lines, but the vast majority of these 2,000 lines are all, like, generated code from these structs and documentation, and bundle, and, like, some integration tests, and the actual logic that this adds is, like.
This stuff, basically.
Though it's not, like, exceptionally interesting in that respect.
And finally, there's this thing.
There's this thing.
Which I am confused about.
Benedikt Bongartz 00:41:05 Yeah, I was looking into this at some point, I think.
Mikołaj Świątek 00:41:10 The problem is that this, this, this becomes a number.
another string.
And I'm not sure where the problem lies exactly.
Obviously, the problem is that we, you know, loaded using some YAML library, and that YAML library decides that this is a number. Yay, YAML, right?
Yeah, but the question is, like, how do you fix it? How do you fix this so that we don't… so that the… because we have to… Load the collector config.
and then Marshall the collector config into a config map, so the collector can load it? Like, how do we… At, like, a structural level, how do we ensure that we don't miss anything up?
Through this process, like we do here.
Because I'm… there's a pull request, wanting to fix this.
Here, right? But this pull request is… kind of… like, just a targeted fix at this specific issue, and I am… yeah, there's, like, some regular expression stop here, and… I am confident that if we have this problem, then we have a bunch of other problems that we just don't know about.
So the question is how to… How to structurally fix this.
So that we know we never… mutate the, collector, configuration.
I… I think we might need to do something like use confap, or… or at least… Whatever that library is called, that I can never remember. Cohen F, yeah, colon F.
But… Not sure if that's actually going to give us a guarantee that we want.
No interest in talking about this.
You want me to… to… Decide on my own.
I don't even know what the answer is, to be honest.
I don't know if Conf is enough, or we… if we need to import CONFMAP from collector car, and I really don't want to import things from collector car, if I can avoid it, especially ConfMap, which is… Quite large and surprisingly complicated.
I guess this is just gonna have to go… Keep… in this farm, until we figure it out. At the very least, I'm not… I don't want to… Do any kind of, like, regex hack.
Around it.
And finally… I think that this might want to un-unick this.
Right, so you're aware people wanted to add the Ruby auto-instrumentation?
And how this should be added is, like, an open question?
And who should be responsible for it?
Anyway, I want to open an issue, or… I think we already… wait a sec, wait a sec. I think we already actually talked about this.
So… Probably… We probably don't want to open the issue, because it's the issue, the issue would say, like.
How do we get the other special interest groups to accept responsibility for these things that we don't want to take responsibility for, which is kind of a rude thing to put in writing?
So… So we don't have a tracker.
Right.
Right now.
Pavol Benedict, are you actually… are any of you actually there, still? Because if there's no one else, then we might as well end the meeting.
Pavol Loffay (Red Hat LLC) 00:47:41 Yeah, yeah, I'm still here.
Mikołaj Świątek 00:47:48 Right. I don't think we need to do anything about this.
Like, it's… More or less clear. That needs to happen.
For these bits, you can look… You can look… we can look at our own pace over here.
I guess the question then would also be… would still be… Do we have anything else that we need to talk about that's not in the agenda?
for today.
You wanna talk about, instrumentation beta Pavol? Is there anything happening interesting in there?
Pavol Loffay (Red Hat LLC) 00:48:36 I was working this week on something else, but I will continue. We need to get the declarative config spec there, which I think is a good timing as well for the Digital Operator PR.
I'm not sure if you want to wait.
Until I have something, or we just merged it, and then we kind of massage it in a way that it… maybe we kind of deduplicate it.
the specs.
Mikołaj Świątek 00:49:04 I don't want to block it.
I think it can go in the way it is.
Pavol Loffay (Red Hat LLC) 00:49:09 And, yeah, on my list, specifically, is to look at the… label selector, how we can use the label selector instead of annotation, and add the reconciler.
Right? I would like to do it in a way that it's, like, off, And we can… Kind of test it internally, and then once we are happy, we could kind of… enable it.
Mikołaj Świątek 00:49:42 That sounds good to me.
Pavol Loffay (Red Hat LLC) 00:49:44 Well, actually, we don't need to reconcile, we just need a Pavolk.
Mikołaj Świątek 00:49:47 Huh.
Jacob.
You back?
There's… there's opinion. You have to… you need to have opinions as the… as a maintainer of this project.
jacob 00:50:07 On, Yuri's issue?
Mikołaj Świątek 00:50:10 Look at this.
There is one thing that nobody else has opinions on.
Where… you know that we have this thing where… where we, like.
Don't delete labels or annotations from resources.
jacob 00:50:24 Yes, yes.
Mikołaj Świątek 00:50:27 there's this change from Yuri, which essentially goes, okay, now we delete things.
But we also expose a configuration, configuration options for labels and annotations that should explicitly be preserved.
jacob 00:50:41 Oh, this is a slippery slope.
Mikołaj Świątek 00:50:45 Wow.
jacob 00:50:45 I…
Mikołaj Świątek 00:50:46 Where does it slip us towards?
jacob 00:50:49 So, I don't like this, because there are a bunch of… the way that this interacts with other operators, I think, is potentially dangerous.
There are issues with this, specifically around, like, Argo CD.
Where, if… Argo adds a label to a deployment, for example. Not the CR.
And we go and we… on each reconcile loop, we see that there's a change and then we go and, remove those, then Argo will go back and add them. This can cause, specifically for labels.
Whenever you make a label change, it forces a new replica set.
Which means that every time that you go in and make a new replica set, or every reconcile loop between ours and, like, Argo or whatever other operators people are running.
You could get into an infinite loop of replicasets and, like, essentially take down a cluster.
We… Could never know the amount of other operations that are happening in the user's cluster.
And I don't think that we are able to effectively fix this.
I think that what we could do is make this, behavior that Yuri wants opt-in.
Such that these things do get removed, but you have to say that you want them to be removed. I don't think that we could have this automatic… this be automatic, because I think if it were to be automatic, then we'd cause massive issues in people's clusters.
Mikołaj Świątek 00:52:25 Okay, so in that case, can you put… can you put this answer under this pull request?
jacob 00:52:29 Yes, I can.
Mikołaj Świątek 00:52:31 Thanks.
jacob 00:52:31 I'll write that up right now. Thank you.
Mikołaj Świątek 00:52:33 Yeah.
jacob 00:52:34 So, yes, I do have an opinion.
Mikołaj Świątek 00:52:36 This other thing, this other thing. Have you seen this? This beautiful, this beautiful issue?
What do you think happens to this?
jacob 00:52:44 Whoa, this is new. I haven't seen this one. I've been, like, looking at the PRs recently and going through.
Mikołaj Świątek 00:52:49 This is true.
jacob 00:52:50 I haven't…
Mikołaj Świątek 00:52:50 A year ago, for the record. Oh.
jacob 00:52:52 That's fine.
Whoa, what do you think?
Mikołaj Świątek 00:52:56 happens with this?
jacob 00:53:01 Is that being interpreted as… Just, like, 12 zeros?
Mikołaj Świątek 00:53:07 It's interpreted as a float, as it turns out, and then we try to marshal it back, we get an error, because we can't.
Look… What happens?
Well, we do marshal it back, but it's a float in the YAML document, and then when the collector tries to read it, it goes, whoa, this cannot be a float.
jacob 00:53:30 Oh, jeez, what's… Oh, wait, where's…
Mikołaj Świątek 00:53:35 Simple, right? Yeah, in ours, we… because this is our config, our structured config, right?
jacob 00:53:42 Yup.
Mikołaj Świątek 00:53:42 So… So, we load it into some structure, and then we marshal it.
I think what actually happens here is that… It's the YAML li… it might even be the Kubernetes YAML library, because the part that parses this into a struct, into, like, a map of string object, right?
is actually Kubernetes itself. It's not us. We don't do anything. We just marshal it back to YAML, Or maybe we do? I'm not actually even sure. Like, I'm basically… I'm wondering… How we can make sure that our, like.
marshal, or un-martial, and then marshal back step.
doesn't change anything in these configurations. Because here, what… the end result of what we do, somehow, is that we start with a string, which also happens to be, you know, a symbolic representation of a… of a number, and this becomes a number along the way.
jacob 00:54:49 I need to understand where in the… in the code this is breaking.
Do we have… does the user have a clear repro in… Like, our codebase?
Mikołaj Świątek 00:55:03 I mean, this is a clear repro.
I don't think they've actually.
jacob 00:55:07 Well, like, have we…
Mikołaj Świątek 00:55:09 happens.
jacob 00:55:11 Yeah.
Mikołaj Świątek 00:55:11 There's an attempt at a fix, and the attempt at a fix goes into config.go, it uses regular expressions, which I am, you know, know.
jacob 00:55:22 Yeah.
Mikołaj Świątek 00:55:22 We're not gonna do that, but…
jacob 00:55:25 No, I don't like this at all. Oh, jeez.
Mikołaj Świątek 00:55:28 There's a custom martial art, I wanna say?
jacob 00:55:32 I don't understand why… but, like, I think that this is a, like, like a… What's the word?
This is a bad fix to this problem, is what I'm.
Mikołaj Świątek 00:55:45 I know, I know it's a bad fix, but I don't know what a good fix is. That's the problem.
jacob 00:55:49 Well, I think we need to understand where the problem is. Is it in this, YAML? Like, is the problem on line, the new line 197?
Mikołaj Świątek 00:56:00 I think the problem, from what I'm seeing, is… Is the fact that…
jacob 00:56:07 Is it that auto-int on line 197 in the YAML encoder?
Mikołaj Świątek 00:56:12 It's possible it's something like this.
jacob 00:56:14 Yeah, that's what I mean, like, to this user, I would just say we should figure out…
Benedikt Bongartz 00:56:19 What is possible.
jacob 00:56:20 causing those.
Benedikt Bongartz 00:56:21 This is a while ago that I was looking into this, I think the main problem was the YAML encoder. So there is a closed pull request, which has just one line changed.
That's what I tried back then.
And, yeah.
Because it's safe?
Mikołaj Świątek 00:56:45 Quote ambiguous values on… And it basically goes through it.
Maybe the problem is that when we load this, the quotes are dropped.
So, from that point on, it gets treated by any, like, YAML marshalling and un-marshalling step along the way, and the round trip just turns it into a… A number, instead of the string that it is.
Like, for me, the question is kind of… What does the collector do?
And can we do exactly the same thing?
Anyway, I don't… I also don't want to, like, keep us all here.
For this specific problem.
jacob 00:57:50 That one, I think, in particular, feels like a bad solution to this issue, and I'd like more investigation.
Mikołaj Świątek 00:57:58 You weren't here, Jacob, so I am also pointing this out to you.
this thing.
jacob 00:58:07 Yep. Is this, well, we talked about this last time, I remember.
Mikołaj Świątek 00:58:11 This is ready. As far as I'm concerned, this is ready, and I approved it.
jacob 00:58:15 Looks like there were merge conflicts that I was waiting on, before reviewing.
Mikołaj Świątek 00:58:20 No.
That's fair enough. I wanted to make sure that we know about this, because again, I don't want to merge this stuff without… One more approval from one of us.
Because it's a pretty big change to the CRD. I don't want anyone to be surprised later by it existing.
jacob 00:58:39 Yeah.
I wonder if we could get, somebody on Declarative Config to also just take a gander at it, and see if it's, Reasonable in implementation.
Mikołaj Świątek 00:58:51 There's a… there's a test in there, which takes… a YAML representation of this structure.
marshals it into YAML, and then unmarshalls it into the clarity config.
jacob 00:59:05 Hmm.
Mikołaj Świątek 00:59:05 So there's, like, a compatibility test.
This verifies that it's fine.
Anyway, that's everything I had.
Do we have any… do you guys have anything you want to talk about?
jacob 00:59:26 I don't think so. I'm… Currently just split-brained between a lot of different things, so it's… That's just the nature of it, though.
Mikołaj Świątek 00:59:37 In some respects, LLMs have made this worse, haven't they?
jacob 00:59:40 Oh, absolutely. I mean, the fact that I can work on, like, 10 projects simultaneously is not good for me. Like, that's… it's a lot of context switching, and it doesn't… and, like.
you know, half of that is open source stuff, and then the other half is, like, internal, like, you know, running, building, startup stuff, which is another beast in itself, right? So… There's a lot…
Mikołaj Świątek 01:00:05 But there, there you can at least, like, ship swap, and nobody will, like… Judge you.
jacob 01:00:13 I mean, I judge myself, but yes.
Hold on! In there, it's like, I can't, I mean, still, like, half of my… like, company work is public, and, like, open source, and is, like, going to be donated to OTEL.
so I need to, like… I need that stuff to be, like, not… Oh.
Terrible. Not in a terrible place, you know.
Mikołaj Świątek 01:00:39 Not, not obviously, not obviously generated by an LLM and then unreviewed.
jacob 01:00:45 I think it's okay, I mean, given that it's just me working on this code, I… this code is not what's being donated, really, it's more the concept of what's been done and, like, how it's been done. More the architecture of it is being donated than anything. I think the code will be rewritten, so… the code itself doesn't need to be of high quality. The architecture and, like, thought behind it needs to be better.
But…
Mikołaj Świątek 01:01:07 I'm running a personal… I'm running a personal project, which is, like, a testing ground for… what kind of guardrails do I actually need to, like, have quality without reading the code?
jacob 01:01:20 Yeah.
Mikołaj Świątek 01:01:21 It is quite… my conclusion thus far is that you can't avoid reading. You might be able to avoid reading Some proportion of the code, but you can't avoid reading all of it.
Eventually, I'll have to read something, even if it's just the tests that check the tests, that's check the, like, the… Yeah. The custom static analysis you came up with to enforce that constraints.
that you're…
jacob 01:01:50 Well, you may remember that, Bene has probably the most complex setup of all of us.
I don't know, Benny, when you were telling me about your, your home, your home setup, I was… I was very impressed.
Benedikt Bongartz 01:02:09 the… thing that I discovered there, so I play with a lot of different models also to see, basically, can I use just a smaller and cheaper model to… overcome issues, and it's usually tests, and I have also a pet project. There, it's also the database.
a Postgres interaction. So if you do migrations or whatever, the LLM does… Weird stuff sometimes.
Those are the only two things that I review for my side project. Otherwise, I don't care. It's just…
Kushagra Shukla 01:02:44 Guys, I'm quite new to this OpenTelemetry Operator, so.
Mikołaj Świątek 01:02:48 Hello.
Kushagra Shukla 01:02:50 Yeah, so, like, I know, like, I have contributed to Collector Contrib, and I was recently looking at this eBPF, OpenTelemetry eBPF, but I don't have Linux machine.
So, I'm just switching back to this, OpenTelemetry collector. So, do you have any issue you want me to take a look at it? Like, for the beginner-friendly, something like that?
Mikołaj Świątek 01:03:14 If there… if there isn't anything marked with good first issue, then…
Kushagra Shukla 01:03:19 Not good for the shoe, but, it's like, could be from easy to medium level, or something like that. If you want me to take a look at it, I'm happy to… Go for it.
Mikołaj Świątek 01:03:37 I don't know if I have anything of… okay, do you have anything in there?
Benedikt Bongartz 01:03:42 Some pull requests to… review and… tests, more or less?
Kushagra Shukla 01:03:51 So from.
Benedikt Bongartz 01:03:51 Gina, she's continuously working on the cluster observability CR.
And… She published a lot of fixes.
And usually what I need to do is… just apply them, test them, so, like, does it work as it should? And… Read the code and see if things work as expected.
I think that would be a good start point.
Kushagra Shukla 01:04:19 Okay?
Benedikt Bongartz 01:04:19 So it's not potentially building some PRs, but… Once her changes are in, I have some other things.
I can create some issues for it.
The good thing here is it's not… Published by default, so we can just… Bye-bye. We can just, experiment a bit.
So for example, I would just send here to the chat some… This here, for example, is something that I have to test, but currently I have a lot. Not enough time, to be honest.
yeah, if you could provide some feedback, just some review here.
Does it work?
Whatever, This would be quite nice. So the idea, maybe to give a short overview, is when you install the OpenTelementary Operator at the collector, it can… it's not so straightforward to get started. For example, you want to get just data into stick notes into Datadoc or something.
you need to understand what data you are collecting, you need to configure, for example, a file lock receiver, you need to configure your host matrix receiver, and then you need to understand how the pipelining works. It's not that this is rocket science, but you need to read about it, and you need to get this up and running.
And the idea with this cluster observability CR, more or less, is to… make it relatively simple, so a user just points to some remote destination and says, I want to send my data here.
And the operator will take care of anything underneath, which means it creates a daemon set, it creates, collects logs for you, it collects host metrics for you, and it will just send it over.
And, the CR is quite new, the reconcile loop on the Operator is quite new, and I think this could be a good Starting point to contribute to the operator, because Yeah, it's best effort right now.
Kushagra Shukla 01:06:21 Yeah, first, I will try to set up this project, like, I'm literally new to this project. I haven't set up yet, so I'm going to set up it, and then I think I can… Like, I can figure it out somehow.
And you just mentioned this pull request, I'm gonna take a look at it as well, and provide some feedback. So, yeah.
Benedikt Bongartz 01:06:43 Yeah, I think the first start point would be get the OpenTeametry collector up and running, like it's usually done, there is some documentation, hopefully it works. If it doesn't work, you can also contribute patches, or sentences, or whatever script.
Kushagra Shukla 01:06:57 to me.
Benedikt Bongartz 01:06:58 Make it more clear for people to understand how to get started, because the last time I was reading the docs, how to set this up is quite a while ago, and I think fresh new eyes are always welcome to Get a perspective, does it actually work as it's supposed to be?
And is the documentation clear enough?
And then you can start playing, maybe, with the class observability CR. If you have some observability backend, like Grafana or something else, you can just send data in.
And hopefully it works.
And once this works, potentially you can check out her pull request, just do a build of all the code on her branch, and then try to get this up and running. And I think At that point, your… on the project, so that you know how it works. You can set it up, you can build and compile new stuff. I think that's a good base for any further contribution.
Kushagra Shukla 01:08:03 To happen, yeah.
Sure, I will take a look at it.
Benedikt Bongartz 01:08:08 All right, I have to drop two, but feel free to just reach out on Slack.
Kushagra Shukla 01:08:13 Sure, sure.
Benedikt Bongartz 01:08:14 Yeah.
Kushagra Shukla 01:08:15 Sean. Alright, yeah.
Benedikt Bongartz 01:08:17 Thank you, see you then, bye.
Kushagra Shukla 01:08:19 Yeah, sure.
Bye.
