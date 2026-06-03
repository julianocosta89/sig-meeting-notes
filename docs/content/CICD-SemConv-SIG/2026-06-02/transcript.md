SIG: CI/CD SemConv SIG
Date: 2026-06-02
Duration: 16 minutes
============================================================

## Zoom Recording Transcript

**Christophe Kamphaus** 00:49 Hello?
**Alan Clucas** 00:54 Hello!
How are you doing?
**Christophe Kamphaus** 00:58 Why aren't you?
I see that Adriel won't be able to join today.
But Carlos will come by.
Let me share my screen, and we can do some triage.
Let's take a look at our board.
I'm not sure if much has changed.
**Alan Clucas** 03:30 stabilization.
**Christophe Kamphaus** 03:33 From my side, I prepared… pull a request for the VCS and attributes, and… CICD as well.
So here, I'd like to ask you… to, review.
the two pull requests I created, so I posted some in Slack.
I will also put some in… In the meeting notes.
If you'd like, I can, go over them with you.
**Alan Clucas** 04:43 Yeah.
I didn't know we were responsible for the, VCS side of things.
**Christophe Kamphaus** 04:59 It's also the CICDSIC who's, managing some.
**Alan Clucas** 05:05 Okay.
**Christophe Kamphaus** 05:08 And it was Adriel and me who, initially defines them. Others were also involved in the SIG at that point, but yeah, right.
We created the initial PRs.
**Alan Clucas** 05:23 Right.
**Christophe Kamphaus** 05:27 When I created some, I also reviewed what we had.
And I found a few, small mistakes and inconsistencies.
I fix, as part of these PRs, maybe I should have created separate PRs, but… Let's see how it goes.
For example, there was one typo for VCS.
And for both VCS and CICD, I noticed that entities did not have attribute roles.
It was something that was defined.
After we created the entities, hence why they were missing.
So, I defined them here because they are necessary in order to stabilize the entities.
So what changed other than that?
It's mostly just a find and replace in the models, replacing development stability with With, release candidates, so, that was straightforward.
But then for metrics, I also had to, yeah, for all the dogs, they had to be regenerated, since they are auto-generated.
And metrics do not yet manage the stability level.
Am I at the right place? Yes, it should be here.
So, metrics do not yet… manage their… a stability level, in YAML.
Okay, I don't find it here, so there was one place I had to replace it.
in the document.
And if I don't find it here, maybe I missed it.
Oh, no, it was this one. So, stability level is actually tracked by hand.
In the YAML layer, wanted to say.
But other documents, like… Like, for CI CD.
there, I had to do some manual changes also in the Markdown documents.
Like, here, as a… Document status, I changed to release candidate.
In Siemachtund.
**Alan Clucas** 08:27 Sydney.
**Christophe Kamphaus** 08:28 Same here.
And for Subras, it was just, replacing stuff in the model.
And regenerating the markdown.
This is what I wanted to say we see.
Entity roles, so I always defined which are identifying.
And which are descriptive.
The idea here is that at some point.
It will be possible to change the descriptive attributes.
On the fly.
As that's… It's a possibility.
And for metrics, only identifying attributes can be used.
**Alan Clucas** 09:18 Yeah.
By the sun, okay.
**Christophe Kamphaus** 09:20 Since they have to stay, Remains the same map all the time.
**Alan Clucas** 09:26 Fightful, yeah.
Throughout the life, I think, okay.
**Christophe Kamphaus** 09:29 Yep.
Any questions so far?
**Alan Clucas** 09:34 And no, nope, it all makes sense.
**Christophe Kamphaus** 09:40 Yeah, so for CICD, it was the same as VCS, I replaced, development with release candidate.
And I also had, again, a few, small sinks.
the entity attribute roles, so here I linked the commits where I changed it.
And, yeah, here's a thousand examples that, Did not contain, actual values from the enum.
I guess at some point we changed the values, and we didn't adjust the examples.
**Alan Clucas** 10:16 Oops.
**Christophe Kamphaus** 10:17 And, here, yeah, 1 of C.
units, I changed to use worker since it's consistent with all the other metrics, where always the unit, Yeah. Is, something I tr…
**Alan Clucas** 10:35 Yeah, count doesn't make a lot of sense, does it? Well… Doesn't tell you anything, especially for a…
**Christophe Kamphaus** 10:41 Yep.
**Alan Clucas** 10:41 a counter.
It's not adding value, yeah.
Okay, that makes sense.
**Christophe Kamphaus** 10:52 Yeah.
was…
**Alan Clucas** 10:55 So, like, where you found the examples has gone wrong, do we have anything that actually proves that?
They are right, or is that just, you know…
**Christophe Kamphaus** 11:04 Basically, I just asked AI to review both our conventions for inconsistencies, and it mentions that.
And then I manually verified that the actual values and the examples Was an actual finding, so yes.
One other thing it mentioned was, We have not defined spans for version control.
That was a question I wanted to ask here.
Should we define some… I guess it would make sense. We could say, check out.
And, if we have any operations with Git.
We could define spans for those.
**Alan Clucas** 12:07 Yes, yes.
Because no matter if you… if you track the network component as a span.
Especially for something like checkout, it's not entirely network, is it?
And you've got completely different… Attributes on that kind of… on a checkout versus a… Hey, should you be gap, whatever.
**Christophe Kamphaus** 12:33 Yeah, and it could also be SSH.
**Alan Clucas** 12:37 Yes.
**Christophe Kamphaus** 12:38 It's.
It, it would be different attributes than if it was just a regular step in a pipeline.
**Alan Clucas** 12:48 Yeah, well, presumably it would be a subspan or by step.
**Christophe Kamphaus** 12:53 Yes.
**Alan Clucas** 12:55 Unless.
**Christophe Kamphaus** 12:55 But if it's trust, then, regular steps, and you would have the command that was executed, but you might be missing which VCS Attributes, are associated to it.
**Alan Clucas** 13:09 Hmm.
Yeah.
Does mate.
It'd be useful to have that information, wouldn't it?
It's harder to know. It depends whether you're… CI system has.
a built-in… Git commands, which a lot of them do, I suppose, so…
**Christophe Kamphaus** 13:38 Yeah, if you have to use an, a certain step, or just execute an SH command to perform the checkouts, and it's more difficult to extract it.
**Alan Clucas** 13:50 Yeah. Still doable, but yes.
I'm…
**Christophe Kamphaus** 13:54 Yes, in that case, you would still track it as an, As a regular pipeline step, but, yeah.
**Alan Clucas** 14:03 Are you… are you thinking of it replacing the regular pipeline stuff, or being… I was thinking of it being a subspot…
**Christophe Kamphaus** 14:09 Eventually, it could replace a pipeline step.
Or… as an, sub-span of a pipeline step.
**Alan Clucas** 14:19 No.
**Christophe Kamphaus** 14:20 But I guess that would be up to… the CICD system to actually implement it in a certain way.
**Alan Clucas** 14:36 Yeah, that does make sense to define them, so…
**Christophe Kamphaus** 14:42 Okay, I will take that as an action item to create an issue for that.
So yeah, that's… Was the update from my side?
I have not heard back from, as a review of my pull request for Jenkins, adoption of Hotel CICD conventions.
There was some, A change in, maintainership there. So there's a new guy reviewing everything.
**Alan Clucas** 15:23 Right.
**Christophe Kamphaus** 15:31 Yep.
Anything from your sites?
And, hi Carlos.
**Alan Clucas** 15:40 I call it.
**Carlos Alberto Cortez** 15:41 Hey, hello.
**Alan Clucas** 15:43 I don't know anything.
**Carlos Alberto Cortez** 15:46 Yeah, likewise.
**Christophe Kamphaus** 15:52 And, yeah, thank you very much for showing up here.
And hopefully… We'll have Adriel back with us next time.
**Alan Clucas** 16:01 Yeah.
**Christophe Kamphaus** 16:03 So yeah, oh yeah.
I asked you to review the two pull requests I added to the notes.
And hopefully, we can get some merged.
**Alan Clucas** 16:20 Yep.
**Christophe Kamphaus** 16:22 So yeah, I will give you back your time.
Have a good week.
**Carlos Alberto Cortez** 16:29 You do? Ciao.
**Alan Clucas** 16:31 You too, see you.
**Christophe Kamphaus** 16:31 Right.
