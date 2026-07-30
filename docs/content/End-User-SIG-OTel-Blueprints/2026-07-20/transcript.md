SIG: End-User SIG: OTel Blueprints
Date: 2026-07-20
Duration: 60 minutes
============================================================

## Zoom Recording Transcript

**Dan Gomez Blanco** 02:28 Hello?
**Mir Ansar Ali Wasif** 02:29 Hey, Dad.
**Lukasz Ciukaj (Splunk Inc.)** 02:33 Hello everyone, sorry for being late.
**Dan Gomez Blanco** 02:37 No problem. I would just hope, Hoping that nobody got on the old… In the old link.
This hasn't… has this length changed?
**Lukasz Ciukaj (Splunk Inc.)** 02:50 I went through the OpenDelemetry calendar, so…
**Dan Gomez Blanco** 02:53 Okay, cool. Because we're changing links, meeting links to the new ones, so, yeah.
**Lukasz Ciukaj (Splunk Inc.)** 03:00 I noticed that here.
Maybe we can paste in our… Slack channel?
**Dan Gomez Blanco** 03:12 Yeah, I just did it.
**Lukasz Ciukaj (Splunk Inc.)** 03:14 Oh, you didn't.
**Dan Gomez Blanco** 03:16 Yeah.
I put it in there as well.
In the notes.
**Lukasz Ciukaj (Splunk Inc.)** 03:41 Bit.
How is it going nice? I'm good?
Well, good. Have a good day.
**Dan Gomez Blanco** 03:54 Yeah, I mean, we're celebrating today, as, like, you know.
**Lukasz Ciukaj (Splunk Inc.)** 03:58 You have some holiday, a public, public holiday?
**Dan Gomez Blanco** 04:02 No, I don't even think it's a public holiday in Spain, but, I mean, like.
I don't know if you've been following the World Cup, but, like, any meeting that I start…
**Lukasz Ciukaj (Splunk Inc.)** 04:11 Oh, yeah, yeah, yeah, yeah, yeah.
That's true. So you're originally from Spain? Yeah.
**Dan Gomez Blanco** 04:16 Yeah, I agree.
**Lukasz Ciukaj (Splunk Inc.)** 04:16 Okay, and you're living in Scotland?
Yeah, congratulations then. Great success.
**Dan Gomez Blanco** 04:22 Yeah, it was cute.
I was like, you know, for everyone else, probably was a really boring game, but if you had any skin in the game, it was, yeah.
**Lukasz Ciukaj (Splunk Inc.)** 04:31 Yeah, it was, you know, great tactic behind that, right? Great defensive playing, so it was good. In the final, obviously, Spain was, like, more offensive than Argentina, but throughout the entire tournament, there was, like, lots of tactics behind that, so great, great playing, guys.
And, yeah, there was a little bit of success on my side as well, because we had some family game, you know, like, just a couple of family members, we were guessing, you know, the results throughout the tournament, like, every day we were, like, putting our guesses.
And I initially didn't work… it didn't work initially good for me. I was, like, surprised because, for example, my sister.
And my mom was even, you know, ahead of me. But then I, in this, you know, knockout round, I started, like, going a little bit up and up in the table.
And then, before the final, I was, like, losing 2 points to the first person on the first place, and 1 point to the person on the second place. And I put 00 for the final, like, you know, the… we were only guessing the, you know, the regular time, so I put 00.
**Dan Gomez Blanco** 05:40 Cool.
**Lukasz Ciukaj (Splunk Inc.)** 05:40 Yeah, and the person from the first place, he put, like, two free, and the second place won two, or something like that, and then I won, like, in the last home game of the tournament, so I'm the family winner of this, of this funny game, but yeah, it's good.
**Dan Gomez Blanco** 05:56 Very nice.
Good stuff.
**Mir Ansar Ali Wasif** 05:59 Hey guys.
I… I'm gonna be video off, because I saw the final match, it was at 1.30am, and I went to bed around 4.35.
**Dan Gomez Blanco** 06:09 Yeah.
**Mir Ansar Ali Wasif** 06:10 Aw.
It was worth it, for sure. It wasn't boring, Dan, 100%. This is what you expect from a final, right? Both the teams giving the 100%.
especially Spain, even the 2010 World Cup was pretty much the same. The game that they played then and now, I can totally relate that, so it was awesome.
**Dan Gomez Blanco** 06:29 Yeah.
**Mir Ansar Ali Wasif** 06:30 Yeah.
So I'll be video off, sorry for that.
**Dan Gomez Blanco** 06:33 That's alright.
So, yeah, Mir, is this your first time joining?
**Mir Ansar Ali Wasif** 06:40 Yeah, this is my first time joining this meeting, yeah.
**Dan Gomez Blanco** 06:43 Cool. Well, you know me, I don't even want to do any intros.
Quick intros, because Mir.
**Mir Ansar Ali Wasif** 06:49 Oh, God.
**Dan Gomez Blanco** 06:49 Together, right? So, yeah.
**Mir Ansar Ali Wasif** 06:52 Hey, Lukas, nice to meet you. So, my name is Mir, I'm based out in Hyderabad, India. I'm a solutions architect.
At, Neural Lake. I work… I do a lot of things in hotel space, and I've been recently pretty much fascinated and interested with what Dan is doing in the Blueprint space, so I decided I would join these big meetings. I'm from… Dan's team as well.
Yeah, nice to meet you.
**Lukasz Ciukaj (Splunk Inc.)** 07:16 Nice to meet you, Mir. So, yeah, my name is Lukaszh, and I'm working as a solutions architect at Cisco Splunk in observability.
And I've been contributing for a while to OpenTelemetry, but nothing significant, I would say. Just a couple of contributions to the Python library, and also End-User Seek, and also the documentation, a couple of blog posts, but then… Dan and I, we met at KubeCon North America last year, so I joined the Blueprints initiative, so now I'm supporting Dan with all of these initiatives.
And yeah, we had a great momentum, I would say, with Blueprints when we announced that. I kind of feel that we a little bit lost it, but we need to regain it, so we are working now to get more people interested in that, get more contributors to OpenTelemetry Blueprints, and move forward with new content.
**Dan Gomez Blanco** 08:06 Yep.
**Mir Ansar Ali Wasif** 08:07 Also…
**Dan Gomez Blanco** 08:07 That's a good segue on, probably a good, it would be a good, time now to have a look at the board and see. So I think one of the things I want to do is basically… Right, so, one of the things that I want to do is ensure that we close the Blueprints project at some point, right?
If we go to… the… is… let me see, if I go to… You want to make sure that the issues that we have in progress are in that board, and then anything else that's not the current priority, we, you know, we put… we put forward after the project is closed, right? So I think that's one of the things that I guess, we… we need to be sure that we have a project, we have some goals, some deliverables as part of that project proposal, and as… as much as it is good to have, like, proposals for the Blueprints, and we can start to work through those, I think it's important that we… that, you know, that we think about closing the project at some point, and then,
**Lukasz Ciukaj (Splunk Inc.)** 09:20 And how it happens that, you know, the items appears here on the, on the… Right.
**Dan Gomez Blanco** 09:25 So there's, like…
**Lukasz Ciukaj (Splunk Inc.)** 09:25 Do you think?
**Dan Gomez Blanco** 09:26 Two ways that you can do that. If you're an approver, in your case, you will have.
**Lukasz Ciukaj (Splunk Inc.)** 09:31 Bitex.
**Dan Gomez Blanco** 09:31 to those issues. So if, let's say, for example, we want to… say… what was the… this one, for example, which is… is in the Blueprints project, but the one that you've been working on, which is…
**Lukasz Ciukaj (Splunk Inc.)** 09:51 improved documentation for Blueprints, deferred from the top, I believe.
**Dan Gomez Blanco** 09:55 Alright, this one, yep. It's not, and the reason why it's not is, you know, you can.
**Lukasz Ciukaj (Splunk Inc.)** 09:59 Oh, okay. Alright, that makes sense. So should we add, like, every single proposal here, for the proposal?
**Dan Gomez Blanco** 10:06 I think we don't… I mean, we'll evaluate if we need to. I mean, the way that, Projects work.
**Lukasz Ciukaj (Splunk Inc.)** 10:15 is…
**Dan Gomez Blanco** 10:15 and I say GitHub projects, is that, some people… you can use them in two ways. The first one, you can use them as, like, a Kanban board, where, like, you know, basically you have some… it's a never-ending type of work, right?
And then, you can also use them, and this is how we use them in OpenTelemetry, to… to have, like, higher level, So roadmap items, right? So if I go to… OpenTelemetry…
**Lukasz Ciukaj (Splunk Inc.)** 10:44 Yeah, okay, I understand, I understand that.
**Dan Gomez Blanco** 10:46 There is a roadmap of roadmaps.
So, like, there's a road… Map projects, that is now archived.
Hmm, okay.
I wonder why this was archived, because this was a… I'll need to follow up with, Where the, with the GC on this, because this was something that we created as part of the graduation… of the project graduation, if there's a better way of… of doing that. So, but yeah, the whole point is that each project in… Mmm…
**Lukasz Ciukaj (Splunk Inc.)** 11:21 Yeah, but I understand that in the… as a project board, we should have only… general issues related to the project, the initiative itself, not the, let's say, what will be produced or create.
**Dan Gomez Blanco** 11:35 Yeah, if we wanted to create another board, we can create another board for, you know, if you want to have, like, Blueprints and reference implementations, as in, like, each of the items that gets created, then that's fine, we can do it that way.
**Lukasz Ciukaj (Splunk Inc.)** 11:45 That would be nice, I think, like, you know, for approvers to have this central view. I was looking for this, actually, like, so we could have a board where you have, let's say, the proposals in review, and… looking for outdoor or something, and then approved on the last… this would be, like, going based by labels. Can we automate it with the labels, or no?
**Dan Gomez Blanco** 12:08 Yeah, you can… You can either automate it with… you can automate it into… so you can't… you can have workflows.
Where you can add things to specific columns, depending on… So you can… this one is disabled at the moment, but for… if we were to enable it in another pro… we can copy this project.
I can actually do this… I mean, I'm fairly familiar with projects.
**Lukasz Ciukaj (Splunk Inc.)** 12:30 That's… it's not mandatory, but I think that would be nice to have at some point. I mean, at the moment it's manageable, we don't have many proposals, but if we have more and more proposals, maybe having this, you know, the central view… I started doing something like that in SharePoint, but if that could be part of GitHub, I think that that would be better.
**Dan Gomez Blanco** 12:47 Yeah, and then we can have them in the different, we can align the columns with the different, steps that we…
**Lukasz Ciukaj (Splunk Inc.)** 12:53 Correct.
**Dan Gomez Blanco** 12:54 Cool, that makes sense. Yeah, but for now, basically, what I wanted to get this There's this… the issues here.
To be, I guess, to be close, and then we can call the OpenTelemetry Blueprints project complete, as in, like, the bootstrap of a project, and then we can continue and be a ute, right? So it's not like… The deliverables in the project have been achieved, and now we're moving into, like.
just Blueprints as a part of, of OTel.
**Lukasz Ciukaj (Splunk Inc.)** 13:23 when the project is closed, do we need to have, like, some review with GC, or some summary of the project, what was done? How does it work, typically?
**Dan Gomez Blanco** 13:31 No, just basically call it as close to, maybe, and I think this is probably something where, like, if we… I saw that, So there was an issue there to basically write a blog post. What I would say is, like, let's postpone the creation of that blog post until we actually get these things done.
Because I would rather have a blog post to call out for further contributions and whatnot.
**Lukasz Ciukaj (Splunk Inc.)** 13:54 Yeah.
**Dan Gomez Blanco** 13:55 When we have the triage process in place, we can have the guidance and the guidelines on the, you know, how to write a good blueprint.
And, yeah, so I guess the things that are missing here… I like… maybe this… we can do a bit of a… Summary status of this.
Do you know what the status is? Alex hasn't been joining lately, but do you know what the status is of the… of the… Blueprint for Kubernetes.
**Lukasz Ciukaj (Splunk Inc.)** 14:27 Nope, I haven't heard from Alex recently, and that's, as you see, last comment I provided, and no feedback.
After that… So, yeah, I can follow up on with Alex on that, if he… or we can do it now.
**Dan Gomez Blanco** 14:43 There's just… I mean, we can follow up on Slack or something, but, like…
**Lukasz Ciukaj (Splunk Inc.)** 14:46 Yeah.
**Dan Gomez Blanco** 14:47 Yeah. Because he wrote something already, I know that there's gonna be some new releases in the…
**Lukasz Ciukaj (Splunk Inc.)** 14:52 Yeah, I think it was pretty advanced, as far as I remember the content there, a couple of minor, you know, comments I had, and also, we should have Sikh review, like, you know, from other Sikhs, but I don't know which one would be the best for this.
Do you have any suggestions here?
**Dan Gomez Blanco** 15:13 Oh, this would be the… The collector and the…
**Lukasz Ciukaj (Splunk Inc.)** 15:18 Collectoria.
**Dan Gomez Blanco** 15:18 And the opera… I mean, the operator people, like, Jacob already was commenting on that, but they're coming up with, with… well, the people in the… in the Kubernetes, semantic conventions Stabilization group.
And yeah.
**Lukasz Ciukaj (Splunk Inc.)** 15:38 So let's wait first on the feedback from Alex, if he wants to continue on that. If he says that yes, then we can suggest, like, other 6 to take a look into what we have currently there.
**Dan Gomez Blanco** 15:50 I mean, if Alex doesn't have… bandwidth, then, you know, it's fine. And then some of us can pick it up, right? I think it's just a matter of, like…
**Lukasz Ciukaj (Splunk Inc.)** 15:58 That's the reason we have these labels, right? We can market as outdoor needed, and start looking for people happy to continue.
**Dan Gomez Blanco** 16:07 Cool. Alright, so you have started, yeah, to work on this, which is basically related to the documentation around the process, right? I guess.
**Lukasz Ciukaj (Splunk Inc.)** 16:17 Yes, correct. So that is the… Last week, I was a bit busy, so I was not able to go forward, but that's on my list for this week, to actually open these PRs and start actually documenting the process, so then we can review it as part of the PR.
And so, yeah, I think it's clear to me what should be done.
I'm just wondering about the labels. Did you see my message that I sent this morning to you and Alolita in the space? About the…
**Dan Gomez Blanco** 16:47 Yeah, so I didn't have time to respond.
**Lukasz Ciukaj (Splunk Inc.)** 16:49 And I put this also in the list of topics to be discussed during this call, so I think that's… That's important, and I would like to see it?
You should see…
**Dan Gomez Blanco** 17:02 Oh, wait.
**Lukasz Ciukaj (Splunk Inc.)** 17:02 Oh, honey.
**Dan Gomez Blanco** 17:03 This one is the… the,
**Lukasz Ciukaj (Splunk Inc.)** 17:06 Yeah, so…
**Dan Gomez Blanco** 17:07 the template, yeah.
**Lukasz Ciukaj (Splunk Inc.)** 17:08 Let me just… Yeah.
**Dan Gomez Blanco** 17:09 Cool.
**Lukasz Ciukaj (Splunk Inc.)** 17:10 attention.
**Dan Gomez Blanco** 17:11 Let's discuss that, yeah.
**Lukasz Ciukaj (Splunk Inc.)** 17:12 Sorry about that, I thought that I… okay, cool. So, yes, I would like to discuss this, and can I share my screen now?
**Dan Gomez Blanco** 17:23 Second, I'll stop chatting.
**Lukasz Ciukaj (Splunk Inc.)** 17:25 Because… give me a sec… That's what my suggestion is.
Okay, What is this one?
Sure, sure, sure… Yeah, so that's the message I sent to you.
**Dan Gomez Blanco** 17:49 Yep.
**Lukasz Ciukaj (Splunk Inc.)** 17:50 Yep, so currently we have these labels created, which is a Blueprint general label for everything Blueprint-related. We have Blueprint comms. I don't know who created that, but for example, the idea of publishing the blog about Blueprints, that's…
**Alolita Sharma (Apple Inc.)** 18:06 Yeah, I did, Lukas.
**Dan Gomez Blanco** 18:09 Alolita.
**Alolita Sharma (Apple Inc.)** 18:10 Hey, hi, hi, you're Dan.
**Lukasz Ciukaj (Splunk Inc.)** 18:12 So, but that's okay, I'm just brainstorming now. So then we have this set of Blueprint labels that we created with Alolita on the last call, which we believe is enough for, you know, taking care of proposals and moving them forward through the process.
But my idea is, I was thinking about that, how to simplify it, because Blueprints and REF implementations are kind of, you know, the same project, right? Same group of people working on that. So I was thinking about, like.
changing the name of this general Blueprints label to something like Blueprints slash ref imps, so that would be everything, like general discussions… Sorry, so let's go.
general discussions, roadmap, governance, publishing, and etc, everything, like, related to Blueprints or Rev Imps, and then separate labels for blueprints, separate labels for reference implementations, but as you see, that's simply the mirror, right? So yeah, proposal needs review, needs out, or in review, and approved, just five.
5 of them. So, do you think that makes sense? Should I go ahead and reorganize it in that way, or should I first open GitHub issue and get some feedback from the community? How do you want me to proceed with that?
**Dan Gomez Blanco** 19:29 I think it's probably… I would probably, yeah, see, I mean, I… to me.
it looks fine. However, yeah, probably put it into the issue, GitHub issue, so other people see it. But one thing I would say is, like, if we look… if the aim is to reduce like, you know, to make it, like, so we don't have, like, so many labels. And the steps are… the same.
**Alolita Sharma (Apple Inc.)** 19:54 Yeah, that's right, Dan.
**Dan Gomez Blanco** 19:55 Can we have two labels? As in, like… sorry, can we have one label that is Blueprints, another one is referenceless implementation?
And then we have proposal, needs review, needs author in review. So it's a combination of the… so basically you can type one with Blueprints.
stream with reference implementation.
**Lukasz Ciukaj (Splunk Inc.)** 20:11 I know what you mean, but then first the label will be long.
is it okay, or not? Or maybe we should figure out some, maybe, short name, or abbreviation.
**Dan Gomez Blanco** 20:22 What I'm saying is, like, instead of, like, using one label.
And we use, like, two labels.
for the… for the triage, right? One label would be in Blueprint.
**Lukasz Ciukaj (Splunk Inc.)** 20:30 Yeah. For example, this and this, right? Blueprint Proposal and Ref Imp proposal.
**Alolita Sharma (Apple Inc.)** 20:35 Oh, I see, I see. Dan, you're just saying that, hey, you know, we have one Blueprint, label, and one reference architecture label, and then the state in another label.
**Dan Gomez Blanco** 20:45 Yeah.
**Alolita Sharma (Apple Inc.)** 20:46 Which is commonly shared. Yeah, that makes sense.
Like, Lukas just having, like, a needs review, needs author, in review, approval, and then it's tagged to the particular object, like Blueprint or reference architecture.
**Lukasz Ciukaj (Splunk Inc.)** 21:00 But would that be clear to everyone, that these are the labels?
**Alolita Sharma (Apple Inc.)** 21:06 We should be. I mean, we all know about it, right?
**Lukasz Ciukaj (Splunk Inc.)** 21:09 neat out or can be used by someone else, right?
**Dan Gomez Blanco** 21:12 We documented… I mean, one of the things that I talked about with the rest of the SIG, and I open an issue for a general, like, end-user sake, is that, now we're getting more… a lot more people, and this is something that Alolitaobi happy to know, because we talked about that as part of a GC in the past, is that we're getting a lot more people interested in APAC to do, like, you know, user sake.
**Alolita Sharma (Apple Inc.)** 21:41 Thanks, but just…
**Dan Gomez Blanco** 21:42 which is great. Yep. But now we're basically, I was in charge, well, just basically, I said, I will volunteer to write, Like a triage document.
or how do we approach that between the two groups, the APAC and the EMEA America group?
And then, for… this is for general End-Us, you know, End-User things, right? Like surveys… tell me sessions and whatnot. So I do think that at the… what my… my intention was that at the general Sagan user thing, we would have, like.
Something that says, well, if it's, like.
you know, if it's general, if it's tagged with general, or tagged with APAC, that has… that's documented there in the… in the general End-User repo.
And then something that says, if it's stacked with Blueprints or reference implementation, then you follow this, and then point to another triage document, which would be the one that we are Writing here.
So in that triage document, as long as you give, you know, the labels… we use the labels, like, proposal, needs review, needs author, and review, and approved.
As long as we document it in that part of the, you know, in that document, we should be fine to use the same label for both, right? Proposal meets review, meets author in review.
**Lukasz Ciukaj (Splunk Inc.)** 23:04 What you are saying is that you would like to simplify it to something like Blueprints?
And ref imps, or… And then have just needs a review… needs outer…
**Dan Gomez Blanco** 23:24 Yep.
**Lukasz Ciukaj (Splunk Inc.)** 23:24 In review.
and approved.
So then we have one for general, let's say, project-related, and then we can use Blueprint and needs review, Blueprint needs outdoor, Blueprint in Review, Blueprint in approach, or reference.
**Dan Gomez Blanco** 23:39 Combination of… combination of two.
In a way, that's sort of the way that it's done in the spec repo, right? Because in the spec repo, you have, like, one label that is, like, metrics, another label that is logs.
And then you… you have, like, triage, Colin.
triage, Colin, needs feedback, or blah blah blah.
That's the way that… That's always that handles it. I don't think we need the triage colon, like, prefix, but, like, if you look at the… At the specification.
Repo.
Let me see.
**Lukasz Ciukaj (Splunk Inc.)** 24:21 Okay, as, like, closing the loop here, I think if you are okay with that, we have more… you have more experience with this, so… so I'm happy to follow this, and I can document that as part of the PR that I will be working on.
**Dan Gomez Blanco** 24:34 Sounds good.
Yeah, I don't think we need the… so, like, let me just show you in a second, like, if I share my screen.
**Lukasz Ciukaj (Splunk Inc.)** 24:40 Yep, go ahead.
**Dan Gomez Blanco** 24:43 Because this works quite well in the spec.
So if you… Yeah, if you see, like, they've got, like, the area, right, is, like, trace, resource, context, metrics, blah blah blah, and they have triage.
deciding to react, accept. I don't think… I'm not saying that we copy this, but, you know, there's two… two different labels.
One that is related to the area, and another one related to the triage.
**Lukasz Ciukaj (Splunk Inc.)** 25:11 to the…
**Dan Gomez Blanco** 25:12 the status, right? Yeah.
**Lukasz Ciukaj (Splunk Inc.)** 25:14 Then you can filter it properly.
**Dan Gomez Blanco** 25:16 Exactly, yeah, then you say, okay, I just want to look at the ones that I…
**Lukasz Ciukaj (Splunk Inc.)** 25:19 Should we, like, use the word triage as well in our labels?
**Dan Gomez Blanco** 25:24 Meh.
I don't know. I don't think… I don't think so. I think we'll… I think if you just had in-review or whatever, I don't think we need to work the triage, Prefix, I think I'll be fine.
**Lukasz Ciukaj (Splunk Inc.)** 25:41 Yeah, we can start with that, we can…
**Dan Gomez Blanco** 25:43 Yeah, we can change it later, it's not like… yeah.
**Lukasz Ciukaj (Splunk Inc.)** 25:46 Alright, sounds good. So, yeah, I like it. Always, you know, the simplification is a good approach, so we have… less labels, we can reuse the labels, and again, as I said, it's the same team working on Blueprints and reference implementations, right? At the moment, at least, so… so we can share these labels. Sounds good. So do you want me still to open the GitHub issue, or just go ahead and share?
**Dan Gomez Blanco** 26:08 Just open the PR, I think, with the… Yeah. Yeah, with the, open it… I guess open it first on the Sega End user repo, right? And then…
**Lukasz Ciukaj (Splunk Inc.)** 26:16 Yep, yeah, but I will open a GitHub issue as well, just to notify the community that we'll be opening this new, or reorganizing labels for Blueprints and recurrence implementations, and I will close it immediately, so just…
**Dan Gomez Blanco** 26:29 Oh, I see. But is it not this, what this is supposed to…
**Lukasz Ciukaj (Splunk Inc.)** 26:33 Hmm, I didn't mention that here, but it could be part of this as well. So, so I… I didn't mention that, it's something I recently figured out.
**Dan Gomez Blanco** 26:44 Ryan, I see what you mean. So I thought this was this… This issue that you were working on.
That would include the changes to the labels.
**Lukasz Ciukaj (Splunk Inc.)** 26:55 Yeah, I mean, eventually it will, but when I was opening this issue, I didn't think about reorganizing labels, so that's, like, I can update this.
issues, man. Yeah.
**Dan Gomez Blanco** 27:07 I think you can, yeah, you can basically have it as part of this issue, and then we… We have the PR for…
**Lukasz Ciukaj (Splunk Inc.)** 27:13 Okay.
**Dan Gomez Blanco** 27:15 Yeah.
**Lukasz Ciukaj (Splunk Inc.)** 27:15 That sounds good. Awesome. That is clear.
**Dan Gomez Blanco** 27:20 Yeah, cool, awesome.
I've not had time to… actually, no, I did have time to work on this. So just an quick update on this. We had, in the front matter of, by the way, I forgot to ask.
Is that… is that good? Asuna, do you need more feedback on?
**Lukasz Ciukaj (Splunk Inc.)** 27:43 Well, you pinged me to review it, and I was a bit confused when I took a look about this.
**Dan Gomez Blanco** 27:49 Sorry, no, there's one. I mean, sorry, do you need more feedback on the…
**Lukasz Ciukaj (Splunk Inc.)** 27:52 No, no, I'm good with that. I can… I will start working on this.
**Dan Gomez Blanco** 27:55 Right, so I'll explain, I'll explain this. So, when we initially created the… The, the first blueprint, right?
**Lukasz Ciukaj (Splunk Inc.)** 28:05 added.
**Dan Gomez Blanco** 28:06 some from matter fields to the templates.
Let me just look at this PR.
So these from matter fields would be, like, author, date, and so on. And this is… this… I mean, I did the same for mine.
Now, the thing is, the reason why these were added originally… was that… When we created the template in the first place, we thought that Hugo.
Could use something like… When you get in, If you come to the blog.
Alright, so I've gone to the blog… you see, they are basically by, you know, Ariel DeMarco, Mande, blah blah blah, right? So… That information is not written in the actual blog post. Prose is actually… you know, HugoDocs will take that information and add it, format it in that way.
Right. So the… so I thought that was what it would do in some way, you know, like, you could just basically point the documents to Hugo, and Hugo would just format it in a nice way. But because we had to do it, as well in, sorry, not for Blueprints, that's another thing. But for reference implementations, sorry, for reference implementations where we do want the author And the… and the date.
we, we added author and CAIC here, and then we also added them here.
So, for reference implementation, as it was… Just a little bit of… Duplicated information, right?
Because you've got that here in the front matter, and you have it again in prose here.
So, I just… it was a matter of, like.
There's no reason for us to have it in two places, right?
That was the first one. That was the change to reference implementations.
The change to, Blueprints is a bit different.
because in Blueprints… because we talked about Blueprints being a living document, right? I guess… It would be like any other type of documentation in the… in the website, so it needs to be updated. And yes, if you go to the history, the author will be Lukasz. But the… but maybe in the future it's someone else, right? I guess that's the thing. That's someone that modifies it, someone that makes a modification to it. And the date, as well, is not something that's been, you know, this is information that is, in a way, hidden. It's not presented anywhere in the Blueprints.
If you open one. So that's why, you know, we… I thought we… we hadn't discussed this, but, like, if we haven't done… Yeah, so… is not anywhere, right? It's not listed anywhere. So… I don't see the point in having that.
Not too much point in having the author and the date.
If this is, like, any other, like…
**Lukasz Ciukaj (Splunk Inc.)** 31:16 But this was never visible, right? It's just a part of the… of the document on GitHub, right? The file on GitHub.
Yeah, okay.
**Dan Gomez Blanco** 31:28 It's not visible, so it was just more like a clean-up of, like, a thing that happened because…
**Lukasz Ciukaj (Splunk Inc.)** 31:31 That's my big update. Alright, yeah. That was something I was a bit confused, because I've seen the suggested change, and then I, okay, but it's not there anywhere on a, you know, in the documentation, but now it's clear, so it's like a cleanup, and…
**Dan Gomez Blanco** 31:45 It's a cleanup as well from the, I guess, in the front matter, like, when we ask people to fill the template.
When we have our templates.
**Lukasz Ciukaj (Splunk Inc.)** 31:53 the same.
**Dan Gomez Blanco** 31:54 End-User repo. Yeah, it's just things that… you know… people have to constantly keep updating the date, when, like, I don't know, like, if there are changes, it makes things a little bit more… You know.
**Lukasz Ciukaj (Splunk Inc.)** 32:07 That's clear to me. Yeah, let's do it.
**Dan Gomez Blanco** 32:10 Cool, awesome. So that's one thing… what else were we? So yeah, so that's in progress.
I have not had time… I think I was going to add some… guidance, or better, or change the issue templates, we talked about that in the past, but if someone else wants to do it. There is guidance on what makes a blueprint good.
in the templates, because we think that is… I think we agreed on this in the past.
And we think that's easier for, let's say, if you're going to use an agent, to help you.
write a blueprint.
That the guidance inside or the guidance about writing a good blueprint should be in comments in the markdown, so that then an agent can use it. However, we also said that, we should… I don't know, publicize that somehow. Like, basically tell people, like… There is a lot of advice in the template, it's not just the template has some… Some, you know… some guidance here.
Is that, like… I guess the whole reason why we created this issue is that we didn't think that we had the guidance on what is a good blueprint and what is a good reference implementation.
We don't have that publicly visible, I guess.
So I guess I'll ask again. Is that something that we want to do, or do we want to, like, create another document that explains the best practice and the guidance? What do you think is the… It's the best way forward.
**Alolita Sharma (Apple Inc.)** 33:47 I think, Dan, Lucas and I were chatting about this a little bit last time.
Because we were trying to figure out, you know, how to better organize, you know, and discoverability of the information that we have around, you know, reference architectures and Blueprints.
And we did think that it would be good to actually have a different page for the best practices, because that also is an area in itself, and it'll continue to, you know, get more refined and evolve.
**Dan Gomez Blanco** 34:21 Sounds good. So I guess, so there's this part here, for example, we could just put in a different document.
**Alolita Sharma (Apple Inc.)** 34:26 Yeah, just a different markdown, and then we can…
**Dan Gomez Blanco** 34:29 stuff that is here, okay.
**Alolita Sharma (Apple Inc.)** 34:31 Yeah, yeah, yeah, because it'll then grow, because one of the things we were, you know, having a bit… we tried it ourselves, and we were like, okay, how do we find this information? Yeah, yeah, no, that's.
**Dan Gomez Blanco** 34:45 That's a good point. I think one of the things is not discoverable, right? Because you come here…
**Alolita Sharma (Apple Inc.)** 34:49 Right.
**Dan Gomez Blanco** 34:50 CNS, and it's like, right, okay.
But if you go… yeah, you need to click… go… you need to.
**Alolita Sharma (Apple Inc.)** 34:55 Yeah.
**Dan Gomez Blanco** 34:55 code, yeah, very well. Yeah.
**Alolita Sharma (Apple Inc.)** 34:57 Cool.
**Dan Gomez Blanco** 34:58 That sounds good. Do you think… So, a document… inside here, right, inside our.
**Alolita Sharma (Apple Inc.)** 35:07 Yeah, exactly, right, right.
**Dan Gomez Blanco** 35:09 Yeah, okay. So we have the templates, and we can basically have, like.
Templates, guidance, or something like that?
**Alolita Sharma (Apple Inc.)** 35:15 Exactly, right. Best practices, whatever we want to call it.
**Dan Gomez Blanco** 35:19 Yeah, template, yeah, templates, best practice, cool.
Yeah, okay. I'll add a comment here later.
**Alolita Sharma (Apple Inc.)** 35:25 And actually, to that, Dan, we were also thinking that if we could have maybe a landing, page, like Blueprints.md or something, in the… SIG user, you know, End-User folder itself.
**Dan Gomez Blanco** 35:42 Alright, okay.
**Alolita Sharma (Apple Inc.)** 35:43 Then it might be… good… a good landing point for, you know, everything that's in the Blueprints repo folder.
**Dan Gomez Blanco** 35:56 Is that… okay.
**Alolita Sharma (Apple Inc.)** 35:58 Because right now, you know, if you look at the, End-User SIG repo, there's a… there's other information too, right? So it's kind of hard to find the…
**Dan Gomez Blanco** 36:11 Yeah. Do you think.
**Alolita Sharma (Apple Inc.)** 36:12 That's…
**Dan Gomez Blanco** 36:12 Do you think it'd be better to change the… the README here, and add a…
**Alolita Sharma (Apple Inc.)** 36:17 Yes, maybe we can if we have a Blueprints section, but Whatever makes sense in terms of just landing in and…
**Dan Gomez Blanco** 36:26 I think it's more… I think it would make it… it might make it more discoverable to say, you know, this is… these are the areas of, These are the areas of the, you know, what is the end-user's sake, for example?
**Alolita Sharma (Apple Inc.)** 36:37 Yeah, yeah.
**Dan Gomez Blanco** 36:38 We can say, well.
there are two primary goals, and that's no longer true. Yeah, that's right. There are three now. There are two primary goals.
**Alolita Sharma (Apple Inc.)** 36:46 It's just fine.
**Dan Gomez Blanco** 36:48 No, that makes sense. That makes sense, yeah.
**Alolita Sharma (Apple Inc.)** 36:50 Or we can just say key goals of the end-user, say, leave it open-ended. As things evolve, you know, we can add stuff.
**Dan Gomez Blanco** 36:57 Maybe a number is not there.
**Alolita Sharma (Apple Inc.)** 36:59 Yeah.
**Dan Gomez Blanco** 37:00 True, okay.
That makes sense, makes total sense. Yeah.
Makes sense. I added a PR here.
Yeah, there's a PR now, basically, to add.
Blueprints, approvers, as there is.
**Alolita Sharma (Apple Inc.)** 37:16 Oh, okay, okay, cool, cool, awesome.
**Dan Gomez Blanco** 37:17 But, you know,
**Alolita Sharma (Apple Inc.)** 37:18 Yeah, because I think it's… it's a bit confusing right now, given that there are two different areas of work going on, right? Blueprints is more deeper, on the technical side, the, End-user comms… comms, work is, you know, also…
**Dan Gomez Blanco** 37:36 Yep.
I have no idea why… GitHub is not letting me apply this change. It's not letting me for data.
**Alolita Sharma (Apple Inc.)** 37:44 I ended up in?
**Dan Gomez Blanco** 37:45 I thought it was an… yeah, I thought it was an ephemeral thing, but, like, I'm logged in, and it just keeps.
**Alolita Sharma (Apple Inc.)** 37:50 Oh, weird.
**Dan Gomez Blanco** 37:51 Could not apply suggestion. I think it got into a wrong… wrong state somehow. I will… I will apply the change, because this… just to make sure that I got this right, Lukasz, this is your… This is your OpenTelemetry one, right?
Luke 6LH.
**Alolita Sharma (Apple Inc.)** 38:10 That's correct.
**Lukasz Ciukaj (Splunk Inc.)** 38:11 Sorry, I'm back, I came back, just came back to my, to my PC. Thanks for updating that.
**Dan Gomez Blanco** 38:16 No, no worries. I mean, I originally wrote this one, and then I was, like, on the go, and I didn't have time to actually commit the change.
**Lukasz Ciukaj (Splunk Inc.)** 38:23 Yeah.
**Dan Gomez Blanco** 38:23 And I added a comment here, but yeah.
**Lukasz Ciukaj (Splunk Inc.)** 38:25 Yeah, I have two GitHub accounts. I, I, I think, I think… And to reorganize it somehow, but yeah, I'm contributing from Look6LH for free.
**Dan Gomez Blanco** 38:35 Alright, cool. Yeah, I'll try to close this one, and then see if this week I can take care of, of, the guidelines and stuff, right? And then I… do you… is it worth… I don't know if I wanted to create a different issue for the rework of, So I might need… I might want to… Yeah, I'll create a different issue, because I want to get input from the… from the rest of the End-User SEG on how we structure that page.
I know they're also thinking about the, you know, as I said, the APAC, team and stuff, so maybe that is, I just want to avoid.
multiple people working on the same document, so I'll just… I think I've got a good understanding of all the things that the End-User Sega's doing currently.
So, there is a lot… there is also a little bit of a change of… Not a lot, but a change of, the charter now that we have… community.
**Alolita Sharma (Apple Inc.)** 39:34 Yes, that's right, that's right, yeah.
**Dan Gomez Blanco** 39:36 reason, Adriana, there are things that they used to do as part of it.
of End-User seg that they're doing now as, like, community managers, so…
**Alolita Sharma (Apple Inc.)** 39:44 Yes, yes, that's true.
Yeah. So, Daniel make the changes, and then… Yeah, yeah.
**Dan Gomez Blanco** 39:51 I will make that, I will make the change.
**Alolita Sharma (Apple Inc.)** 39:52 Yeah, we can review, help review.
**Dan Gomez Blanco** 39:55 Thank you very much.
Cool. Right. I… now that Alex has joined… It's just like… Have you seen my… have you read my comment? And then join the call, Alex.
**Alexandre Ferreira** 40:07 Yeah, I got summoned, doing good. So, I was checking the PR yesterday, I think?
And they should provide some updates, this week, hopefully today.
And… I had a few stuff with my daughter, and, like, couldn't do it last week, but, I will implement the suggestions we discussed on the last call.
And also the ones that I see, from Lucas and you, then, from… Two weeks ago, boards.
But yeah, and I hope this is… Closer to, to being, merged.
**Dan Gomez Blanco** 40:53 Awesome. I will… I've not had a chance to review it yet, but… this… the PR is… is it in a draft, or is it…
**Alexandre Ferreira** 41:05 Some, some drop.
Should I keep this PR there in OpenTelemetry that I wrote, or should I open one in the second user?
**Dan Gomez Blanco** 41:16 No, no, no, I think that's fine. I think you're good.
It would be this one, yeah.
**Alexandre Ferreira** 41:24 Alright,
**Dan Gomez Blanco** 41:26 Cool. So I guess the action here for it…
**Lukasz Ciukaj (Splunk Inc.)** 41:28 I mean, it looked good to me, as far as I can remember. The only one that I was missing was kind of, you know, some diagram, or something more, like, visual, because that was pure text, so if you could, like, think about, you know, adding some, I don't know, decision tree, or something that I put or done in Blueprints, I think that makes this blueprint more, like, interactive.
interactive.
**Dan Gomez Blanco** 41:50 Oh, yeah.
**Lukasz Ciukaj (Splunk Inc.)** 41:51 just read it, and consume, not just a pure text. So if you could consider adding something, that would be great. And as we discussed with Dan before you joined, we would like someone from the collector SIG, or maybe one more SIG to review it as well from their perspective before we proceed with merging.
**Dan Gomez Blanco** 42:10 Yeah.
**Alexandre Ferreira** 42:11 And I'll also… Remove some of the manual code that's there, because, ideally, we will only reference existing material, right, so that we don't have to update this if something changes like this. Yeah.
like, this, this little snippet right there, we should, like, only perhaps mention that you have the presets, and then some diagrams on how the presets work, the plan went versus Lumen, and call that a thing.
And also, Lukasz would send some, comments. There's some inconsistencies.
**Dan Gomez Blanco** 42:55 Nope, nope, we lost you. I think you're…
**Alolita Sharma (Apple Inc.)** 42:59 Yeah, I can… we can't hear you anymore, Alex.
**Alexandre Ferreira** 43:05 Can you hear me now?
**Dan Gomez Blanco** 43:06 Yes.
**Alexandre Ferreira** 43:10 Hello?
**Dan Gomez Blanco** 43:11 Yep, we can hear you.
**Alexandre Ferreira** 43:12 My, my, my AirPods died up.
there are some inconsistencies below, or, like, there's some sections that are missing some numbers, because I refactored and removed some stuff. So you have, like, 0.4 going… jumping all the way up to 6, so although we will, refactor all of that.
Yeah, I should have sent a message… In the channel, once it's done for reviewing.
**Dan Gomez Blanco** 43:41 One thing… one thing that I had a… I had a question here on… More of a general question.
we… we left… I mean, I think one of the things that we wanted to cover was how to monitor certain, like, you know, like, standard components in Kubernetes, like, you know, Core DNS or CNI, and so on. However, is there anything specific about them… That is not just using the Prometheus receiver?
As in, is there anything OTel-specific about them? I'm just trying to think if they can all be, like, you know, joint into one, like, hey, you know, to monitor these, like, OTel… native… sorry, sorry, non-OTEL native, like Prometheus native components. We recommend using the Prometheus receiver, and then blah blah blah, like, without having to list every one of them, maybe?
**Alexandre Ferreira** 44:33 Yes, so the, remember we discussing this, so instead of… will do just as you mentioned. So, like, if you don't have OTel native, components, here's how to instrument them. I will not tell you which metrics or, which component to actually, monitor, but, Here's how to do it in Prometheus.
**Dan Gomez Blanco** 45:01 Cool, yeah, that's it. So that's something that you hope that you can work on soon, or…
**Alexandre Ferreira** 45:06 Again, sorry?
**Dan Gomez Blanco** 45:07 Is that something that you're planning to work on soon?
**Alexandre Ferreira** 45:10 Yeah, I… hopefully today, I have some free time in the afternoon.
And I will stop.
**Dan Gomez Blanco** 45:17 Nice. And if you wanted to, you know, maybe that's the sort of thing where, like, if you wanted to… I don't know.
If you wanted to add more context, there's always the appendices, right? You can add an appendix for it, if you wanted to add more stuff, if you needed something specific, but yeah.
**Alexandre Ferreira** 45:35 That looks good.
**Dan Gomez Blanco** 45:36 Awesome. Great. I will keep an eye out for the changes, I will review this, and I guess I'll urge everyone else to do the same.
And then… Yeah.
**Alexandre Ferreira** 45:47 One other thing that I've pivoted in the last, change that I've made.
I'm not… suggesting, like, CubeSat metrics and CADvisor anymore. I think if you go a little bit down, I'm suggesting the OTel native ones, like host metrics, receiver, there you go.
**Alolita Sharma (Apple Inc.)** 46:05 Nice, nice. That's good.
**Alexandre Ferreira** 46:07 Prometheus components, just in case someone remembers the old way, and then say, oh, yeah, Case Cluster is the same thing as QC. Nice.
**Dan Gomez Blanco** 46:18 Yeah, one thing that I was… that I was thinking is, I've seen a lot of end users now… Using the… the OpenTelemetry KubeStack.
Is that something that we… so the OpenTelemetry CubeStack as the, you know, the chart that would… do all these things. I do not know… I know that, for example, probably Jacob.
I think he commented on the original thing, but maybe Jacob knows more about that, because he's… part of the operator in the Helm charts, SIG.
if… what's their recommend… you know, what's their way forward, actually? Is it, like, doubling down and using the… the OpenTelemetry… OpenTelemetry CubeStack?
Or is it, keeping the individual charts with the presets, as you're mentioning there.
**Alexandre Ferreira** 47:15 Yeah, I don't know.
**Alolita Sharma (Apple Inc.)** 47:16 Yeah, that's a good call-out. I think we should probably, Alexa.
Check in with, the operator team.
**Dan Gomez Blanco** 47:25 Yeah, I think if we tag them, then we can…
**Alolita Sharma (Apple Inc.)** 47:27 Yeah.
**Dan Gomez Blanco** 47:27 Yeah, if anyone wants to tag them, And say, you know, what's… What's the, you know, the long-term recommendation here, as a…
**Alexandre Ferreira** 47:37 So, is there a GitHub team called Operator Team that, if I mention them, all of them will see it?
**Alolita Sharma (Apple Inc.)** 47:44 Yeah, there's a OTel collector operator, for example, group.
**Dan Gomez Blanco** 47:50 You're… you're part of the… you're part of the… are you part of the organization?
**Alolita Sharma (Apple Inc.)** 47:54 Are you a member, Alex, of the OTel?
**Alexandre Ferreira** 47:58 I don't think so.
**Dan Gomez Blanco** 48:00 Because that is a limitation.
**Alolita Sharma (Apple Inc.)** 48:02 I think, yeah, I think, I think it's hard to, hard to, get things ping folks.
**Dan Gomez Blanco** 48:09 Yeah, you cannot ping teams if you're not a member of the org.
**Alexandre Ferreira** 48:14 Oh, it's.
**Dan Gomez Blanco** 48:15 But we… one of asking at them.
So it's all pretty…
**Alexandre Ferreira** 48:19 surfing?
**Dan Gomez Blanco** 48:20 Operator approver.
**Alexandre Ferreira** 48:22 Hopefully, when this gets merged, this will be my tribe by fire, and then join the community, perhaps.
**Dan Gomez Blanco** 48:28 Yeah, absolutely.
We love to have more folks.
**Alolita Sharma (Apple Inc.)** 48:33 Yes. Absolutely.
**Dan Gomez Blanco** 48:35 If, yeah, you.
**Alexandre Ferreira** 48:38 I'll let you know on Slack whenever I do that, and then you can mention, can CC the operator team that.
**Dan Gomez Blanco** 48:45 Cool. So, next steps here, if you, like, you know, apply some of your latest changes that you wanted to apply.
Let us know, then we can do another, you know, review, and then, and then tag the… the operator and the helm approvers, I guess, I guess.
**Alexandre Ferreira** 49:03 Okay, I'll do that.
**Dan Gomez Blanco** 49:06 Okay.
Anything else?
**Lukasz Ciukaj (Splunk Inc.)** 49:13 I'm good.
**Alolita Sharma (Apple Inc.)** 49:14 I think, one thing, Dan, I'll find an issue for it. One of the discussions, that, we were having in the tab today, was on, you know, as OTel semantic conventions, is going to work closely on the sustainability, semantic conventions, for metrics.
Yep. So, that is something that, again, would be nice to see as a blueprint.
So I think it's an, you know, an area which is very directly related to energy efficiency, but also to cost measurement, especially for AI infrastructure. So, I'll open up an issue in terms of just the… area of interest, but it might be something that, you know, we kind of get more folks, especially from the sustainability TCG under, you know, which is, which is focused on that, to be able to also contribute there. So,
**Dan Gomez Blanco** 50:21 That'd be awesome. There's also the, well, you're aware of that, the Green Softwork Foundation, that is…
**Alolita Sharma (Apple Inc.)** 50:26 Yes, yes, they are collaborating, right, with the semantic conventions group, so I've been working with them on the… On their end, you know, with the tag, to get them more, more, onboarded, but they'll start, you know, this week, right? So, that should be cool to get them involved early.
**Dan Gomez Blanco** 50:50 Yeah, I'll try to keep an eye on that as well. I did say that I would… volunteer, although I don't… it's not my area of expertise, but I'm interested in the… in the SCI, like, formula.
**Alolita Sharma (Apple Inc.)** 51:01 Yeah, yeah, yeah. I mean, again, I think it's a really, timely initiative because of just the… You know, overwhelming, sustainability or energy factors, if you will, which, again, factor in, you know, very directly into infrastructure being built out and measured, for For cost.
**Dan Gomez Blanco** 51:25 Yeah, that would be cool. Right, so if you can… if you can do that, yeah, we can start together.
**Alolita Sharma (Apple Inc.)** 51:29 Yeah, I'll open up an issue, and then we can at least, you know, get that thread.
actively going, and then we can, you know, figure out how we get a reference implementation in. I talked to the CERN folks,
**Dan Gomez Blanco** 51:44 Huh.
**Alolita Sharma (Apple Inc.)** 51:44 Maybe we could get their blueprint, in.
Because they do use OTel, you know, and that would be a nice, nice example. But I'll follow up on it, I just wanted to let you know.
**Dan Gomez Blanco** 51:58 That'd be awesome.
Thank you very much.
**Alolita Sharma (Apple Inc.)** 52:00 Totally.
**Dan Gomez Blanco** 52:02 Alright, I guess we'll… Have a few actions to follow up on, but So, you know, these days, I'm so used to, like, some, like, AI taking notes, for me, there's one of the things that I think we… is I would like… I would like this to be emailed to me, please. All the actions in the notes.
**Alolita Sharma (Apple Inc.)** 52:19 Yes!
**Dan Gomez Blanco** 52:21 Because I can't take notes anymore in meetings.
**Alolita Sharma (Apple Inc.)** 52:26 I think, I think maybe, I think some of the, Meetings do, with permission to, you know, enable the notetaker, so…
**Dan Gomez Blanco** 52:36 You could do that.
**Alolita Sharma (Apple Inc.)** 52:36 that, if that's.
**Dan Gomez Blanco** 52:37 Another, yeah, another have the new, the new Zoom org, maybe, yeah.
**Alolita Sharma (Apple Inc.)** 52:42 Yeah.
**Dan Gomez Blanco** 52:43 I mean, we have the transcripts, right, available.
**Alolita Sharma (Apple Inc.)** 52:45 Hitrate.
**Dan Gomez Blanco** 52:46 We can, we can do that.
Actually, yeah, maybe I'll… I'll start doing that.
**Alolita Sharma (Apple Inc.)** 52:51 Yeah, we can enable it,
**Dan Gomez Blanco** 52:53 Well, the transcript is there, so we can just basically feed that, and then do the summary… Yes. Do the summary after, right?
**Alolita Sharma (Apple Inc.)** 52:59 And we can just post it even to, you know, to the folder.
**Dan Gomez Blanco** 53:04 Mir.
**Alolita Sharma (Apple Inc.)** 53:04 That's useful.
**Dan Gomez Blanco** 53:06 Absolutely.
Awesome, right? Well, I'll see you in the next one.
**Alolita Sharma (Apple Inc.)** 53:10 Thank you.
**Dan Gomez Blanco** 53:11 Bye-bye!
**Alolita Sharma (Apple Inc.)** 53:11 Thank you, everyone. Take care.
**Lukasz Ciukaj (Splunk Inc.)** 53:13 Thank you all. Bye.
**Alolita Sharma (Apple Inc.)** 53:14 Bye.
