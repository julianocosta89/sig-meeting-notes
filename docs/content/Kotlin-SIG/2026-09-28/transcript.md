SIG: Kotlin SIG
Date: 2026-09-28
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**DavidGrath** 01:12 Hello.
David, you have a lot of background noise.
**Jason Plumb** 01:30 Thank you.
**Jamie Lynch (Palo Alto Networks)** 01:33 Thanks.
**Jason Plumb** 01:34 It literally sounded like you were in a server room.
**Jamie Lynch (Palo Alto Networks)** 01:44 Well, I'll just give it a minute or two for folks to add items to the agenda if you have anything to discuss.
Yeah, I know that Hanson's not going to be here today, he's not… Feeling 100%.
**Jason Plumb** 02:06 Yeah, but I'm still distracted by some stuff.
Probably for at least another week.
**Jamie Lynch (Palo Alto Networks)** 02:12 Mmm.
**Jason Plumb** 02:13 Hopefully, it's not too much longer, but we'll see.
**Jamie Lynch (Palo Alto Networks)** 02:17 Yeah, fingers crossed.
**Jason Plumb** 02:19 Yep.
**Jamie Lynch (Palo Alto Networks)** 02:27 Oh, I guess we can just make a start, and if folks think up.
Items we want to discuss, then.
So we can add them as we go.
So, this was the first item, so we had a PR come in.
But it's basically adding support for TV OS targets.
So there's a little bit of discussion.
on this issue.
where someone basically was using a Kotlin multi-platform project that supports Apple TV.
and was requesting support for this.
So, someone has come along.
And… Added support.
So, I think my… Question on this is basically, like.
What's the bar for adding support? Do we need… And how do we maintain it going forward?
So this is just basically adding the build target.
Do we need anything else beyond that?
**Jason Plumb** 03:42 It's a good question. What are you thinking, or what are you getting at? Because I can't… I'm not.
Nothing stands out to me as extra immediately.
**Jamie Lynch (Palo Alto Networks)** 04:00 I mean, I think I'd be happy accepting… That sort of change as it is, where we're just adding a build target.
And there's not necessarily any dedicated support.
I think… As long as we're documenting that… There's much less testing when compared to, like, the JVM or Android targets.
**Jason Plumb** 04:27 Sure, yeah.
What kinds of things do you think would be required to provide additional support, or is it just that it's unknown? Like, we just don't know?
Like, I've got no way to test this, like, on a real device.
**Jamie Lynch (Palo Alto Networks)** 04:43 Yeah.
I think.
I guess it's like a… Different tier of support, like, just making sure that it compiles is probably the lowest bare minimum.
efforts, then… like adding to an example app or getting some sort of test that asserts that the SDK isn't going to immediately fall over would be the next step.
Yeah, it's… Then probably closer to what we've got for JVM and Android and like.
All the smoke tests would be… the final tier.
**Jason Plumb** 05:25 Yeah.
I mean, so they say something about test resources used by native tests are now copied into the TVOS simulator test bundles?
In the PR.
I don't know what that means. I haven't looked at this piece.
**Jamie Lynch (Palo Alto Networks)** 05:38 Yeah.
So… I think it would be this. Basically, it adds a… Gradle task to… copy over, Because it's a Kotlin multiplatform project and not like a JVM project, there's not like the equivalent concept of like a resource directory. So you've got to kind of manually copy files over to read a resource.
**Jason Plumb** 06:09 Got it. Okay, that's all that's saying. Alright.
Yeah.
I guess that's helpful.
Yeah, it would be cool if this person that picked up the PR could give us some more… like, I think it's probably fine to go forward with that, but it'd be cool if the original PR author could give some more… details around their interest in TVOS.
Or if they just, you know, have an AI on their side and they're just going and picking up issues that are open, you know. Yeah. Because that's happening everywhere right now.
**Jamie Lynch (Palo Alto Networks)** 06:51 True.
**Jason Plumb** 06:52 Yeah.
Which is, I mean, it's also not maybe the worst thing in the world, but, like, it doesn't… it can… I think it has the potential of just Dramatically increasing maintainer burden and long-term maintenance load.
**Jamie Lynch (Palo Alto Networks)** 07:10 sense.
**Jason Plumb** 07:10 Yeah, but it'd be cool if they're like, you know, if they're like a really actually interested in the project, and they have opinions on it'd be cool to know that. But.
I think we can ask them, and they probably won't ignore it, but we'll see.
Okay. The PR is, like, a weird place to do that, but I think it's fine.
**Jamie Lynch (Palo Alto Networks)** 07:28 Cool, so we can ask on the original issue of the PR what the interest is in, and yeah, then we can… Kind of… I'll have a pop over here, and… Yeah, see what we need to change, if anything.
**Jason Plumb** 07:43 Cool. Yeah, because if they have a realistic application, like, maybe they've got some ideas, too, on how to… Next steps for testing it, or whatever.
**Jamie Lynch (Palo Alto Networks)** 07:52 Makes sense.
**Jason Plumb** 07:54 And the fact, like, it suggests that there is a simulator available.
Which is at least something, but I've never… yeah.
**Jamie Lynch (Palo Alto Networks)** 08:01 Yeah, it was a… I don't think I've ever used it, but is a simulator, as far as I'm aware, but definitely is for iOS.
**Jason Plumb** 08:10 Makes sense.
**Jamie Lynch (Palo Alto Networks)** 08:11 Sure, it's for TVLs.
**Jason Plumb** 08:13 Okay.
**Jamie Lynch (Palo Alto Networks)** 08:16 Cool. Yeah, the only other thing to mention, or the only other thing I had to mention is a bit of an update on the publication API. So I've been kind of talking to Carlos and… Yeah, we just kind of, like, summarized… or clarify some of the requirements.
So I've kind of like written it down here, starting from what my assumptions were.
But basically, like, Best Bet has kind of, like, the key… requirements, so we need the SPAN context and baggage.
to… It needs to be possible to create an instance of them from the API module.
**Jason Plumb** 09:04 With no additional dependencies?
**Jamie Lynch (Palo Alto Networks)** 09:07 Yes, so that's gonna require… Shifting a bit of code around and making some changes, but I've…
**Jason Plumb** 09:15 Yep.
**Jamie Lynch (Palo Alto Networks)** 09:16 Make a start from that. And I think we came to a conclusion with.
these constraints that the combat module will need to kind of have a bit of a, like, marshalling step, so that it can use those, Kotlin objects.
So… It's introducing a bit more Kotlin into the compatibility layer, but it feels like the consensus is that should be okay.
**Jason Plumb** 09:46 Makes sense to me.
**Jamie Lynch (Palo Alto Networks)** 09:48 Cool. And… He also had a little look at what the context implementation did, on JavaScript, because they're in a similar kind of scenario where they have an API definition, and then it needs to support, like, browser and server.
So there's… Basically two separate packages in the JS repo.
And then the user basically conditionally imports The one that is appropriate for their environment.
So… I'm… La Shorte on… Exactly how we'll do that, but… That's a bit later on in the story, I think.
**Jason Plumb** 10:43 Okay.
**Carlos Alberto Cortez (Dash0)** 10:46 Sorry for being late. Thank you for discussing this. Yeah, happy to talk a little bit more.
**Jamie Lynch (Palo Alto Networks)** 10:55 Cool.
I was just kind of, like.
Going over what we, kind of, discussed about last week via Slack, so… I feel pretty happy with, like, the span context and baggage changes, and… Yeah, I'm happy with, like.
For context changes, in principle, I… just need to… Progress a little further and see what it's gonna be like.
providing separate packages for context, then I might have a few more questions.
But yeah, I don't really have anything else to add, Bill?
**Jason Plumb** 11:51 I think it's good to see these stated like this, and I think it is not surprising where we're ending up.
**Jamie Lynch (Palo Alto Networks)** 12:00 Cool.
Okay, was there anything else that folks wanted to discuss?
I guess we can all get some time back then.
**Jason Plumb** 12:22 Hopefully I can do some reviews soon.
**Jamie Lynch (Palo Alto Networks)** 12:25 Yeah, fingers crossed.
**Jason Plumb** 12:28 Thanks.
**Carlos Alberto Cortez (Dash0)** 12:29 Thank you so much.
**Jason Plumb** 12:30 Take care, everyone.
**Jamie Lynch (Palo Alto Networks)** 12:31 Okay.
**Jason Plumb** 12:32 Right.
