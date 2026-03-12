SIG: GC Project Management (EU)
Date: 2025-06-16
Duration: 54 minutes
Zoom Recording URL: https://zoom.us/rec/share/AV2BB66Nk7oWWXdH7DJMFUAo2WNmJHiIlg14304_HboPWEJuu5iDEd95DPOzKDBn._fJNUogwdjMWZT0K
============================================================

## Zoom Recording Transcript

**Dan Gomez Blanco** 01:48 Morning.
**Robert Pająk** 01:50 Hello!
Can you hear me?
**Dan Gomez Blanco** 01:52 Yep, all good.
**Robert Pająk** 01:54 Awesome.
I guess Severin will join because he created the channel today. That's my guess.
Us is also online.
**Dan Gomez Blanco** 02:10 Is. Yeah, I don't know. I don't know who's going to join.
Oh, right. So, Severance said that he'll join 20 to 30 min after the hour.
See, I just read that now.
Do you wanna come back here for that, or do you? Wanna should we crack on? You must, you know you and I.
**Robert Pająk** 05:00 Whatever your preference, but I thought that you cannot join the second half right.
**Dan Gomez Blanco** 05:05 I can.
Yeah, basically.
I could join like the 1st half of the second half. But now that I'm here, I guess you know it makes sense that we just go through it. Yeah.
let me just get a new window up.
There's only one to triage actually.
and let me share my screen.
Which is this one.
**Robert Pająk** 06:06 Woohoo!
At least, let's see.
**Dan Gomez Blanco** 06:15 Maximum tension value?
Right? I think I read it.
unsure about this one, because this would be at what point do you actually store this.
I mean, if you have a if you wanted to have like something like a Max.
**Robert Pająk** 07:43 My only idea is to ask Semitic conventions if they want to provide them. I don't know. Somewhere in the realm or somewhere there, I think they are the best representatives to take a 1st look at it like they have this, you know, descriptions of values, etc, and I'm maybe they already have something like that which I am not aware of.
**Dan Gomez Blanco** 08:08 That is true. I mean, there are possible values right and stuff like that. But like for like for enams, for example, it would be like.
**Robert Pająk** 08:17 Yes.
**Dan Gomez Blanco** 08:17 Values right? But yeah, I just think that basically, from the perspective, I was just thinking from the perspective of like having it in the you know. Some something in the metric description is, or it's parallel, I guess, to the metric description.
What would happen, for example, if you had, and metric view.
That then will will that change the Mac, you know. Will that change that the the property?
Have you had a metric view on top of it.
because you're doing the last value instead of a sum, and then it's no longer like the same doesn't represent the same thing.
So I know where this is coming from. I can get the problem. I'm not sure if a metric description is as the right place to put it.
So I guess you know, from the perspective of triage.
**Robert Pająk** 09:19 I mean, I mean that in my opinion, this based on this description, there's nothing to be in the data model. We need to know the Apis just about the scheme.
**Dan Gomez Blanco** 09:34 Yeah.
**Robert Pająk** 09:36 I don't know. I'm not sure if we can ask semantic conventions to handle it. I'm not sure it's possible to try it, or I don't think we should move it there right now, but maybe just. I don't know csing this. I'm not sure if there are some dedicated maintainers for the semantic conventions metrics. I think they are.
**Dan Gomez Blanco** 09:58 I think this almost like feels like something that the so I know that the folks in Weaver more things.
having something that can validate telemetry or telemetry stream, as it goes, you know. Basically.
according to our telemetry schema.
So if there's in the schema then, and you could validate it. Then that will probably make yeah, make more sense. Yeah, okay, I will do that. Let me just have it. As like deciding.
**Robert Pająk** 10:32 Comment, yeah.
**Dan Gomez Blanco** 10:32 Community hub, community feedback, and they know Quinn Tag.
This is saying, Conf. General, same Conf.
**Robert Pająk** 10:55 Is there metrics?
No, okay. So probably just maintainers, probably.
And they can just discuss it.
**Dan Gomez Blanco** 11:05 Let me go. What? What teams do we have for Sancom?
Quite a lot. Same com.
She's just a sink of maintainers. Yeah, I guess.
**Robert Pająk** 11:25 Yeah.
**Dan Gomez Blanco** 11:25 Yeah, but specs sent on maintainers. That's why I didn't find it, I think.
Yeah.
no. I say, this.
**Robert Pająk** 12:57 That's perfect.
**Dan Gomez Blanco** 13:00 Let's do that.
And yeah, and that's it. That was the only one I can do the follow-ups.
**Robert Pająk** 13:20 Nothing to follow up might be a perfect.
**Dan Gomez Blanco** 13:24 Let me just have a look at the community. See if there's any issues here that need to be adding as well.
And I think we did. Yeah, I remember, Pablo, yeah, mentioned this.
Yeah, okay, so these haven't been triaged.
4.
All the reasons.
**Robert Pająk** 13:53 There is one thing which are not sure if you're aware of. So in the auto Maintainers Slack Channel Trust, recently shared that he has been doing some changes in open telemity organization and the code owners. I automation has stopped working for at least collector and go country.
**Dan Gomez Blanco** 14:23 Yeah.
**Robert Pająk** 14:23 And there were some proposals like different points of view. Should we just add the code owners to 3 azures? Or should we just create a new role like code owners. And I'm not sure whether any further discussions around it or to reverse from the rule, because we thought from the go perspective.
that we will just add every code owner as a treasure. But we already got a push back that people are being afraid labeled as treasures, because I think they feel that it's a may be a bigger, more, broader responsibility.
At least, maybe just about improving the community docs, so that people are not so afraid of being a treasure. Because right now, the the role people like a project management stuff, basically that someone is basically responsible for adding labels responding to issues, whereas our idea about adding code owners is just to give them powers so that they can be at labels. The issues.
then can be assigned without any problem.
Because they'll be basically part of the repository team when there are 3 azures, because basic. Yeah. So basically, that's it. We are just want to give them power, but we do not risk. We do not want them to have the responsive to make it clear that they are not. They do not need to participate in, you know, setting up milestones and things like that.
**Dan Gomez Blanco** 15:55 Okay, yeah, it makes sense. And you think that is something that we should include in the and the guidance here?
Or is that something that is like.
**Robert Pająk** 16:04 I'm not sure. I I think that I see, like probably 3 possibilities, one is to create a separate role which will be like, you know, Code owner, because I think that they're all. I think this is something that may be beneficial for more 6. I think that I know that Dot also has code owners for each component. I guess Java has as well.
So one. So the possibilities at the new role.
This is one possibility. Second is to maybe make the description of the treasure more. I don't know. Flexible that it can be someone who, you know basically is responding for this, or is basically just a code owner or some specific thing, and he is not an approval for the whole, you know section. But he may be responsible for subsection.
This is second possibility, 3rd possibility. I don't know what stress did, but basically reverting the changes that requires us to add people to to, you know. Just add people to their repositories.
So I see these 3 possibilities.
**Dan Gomez Blanco** 17:17 Yeah.
Hmm.
**Robert Pająk** 17:22 I'm not sure if there's an issue for it or not.
**Dan Gomez Blanco** 17:24 I don't remember.
**Robert Pająk** 17:25 Maybe it's this one. Supporters see who can brush machine. But I'm sure I if you go to slack auto Maintainers, maybe there's some issue.
**Dan Gomez Blanco** 17:36 Alright! Let me just and.
**Robert Pająk** 17:40 It's like, probably.
**Dan Gomez Blanco** 17:42 Oh, I see!
**Robert Pająk** 17:43 Bottom or something. Yeah.
**Dan Gomez Blanco** 17:46 Is that the one that Damien.
**Robert Pająk** 17:49 Yes.
**Dan Gomez Blanco** 17:50 And there was.
don't see any issue there apart from like the Pr. That they linked. Oh, no, right. I see this support. Private repos in the there was an unforeseen side effect here.
**Robert Pająk** 18:20 So they created a separate.
**Dan Gomez Blanco** 18:23 So there's the open telemetryprivate. Org. Yeah.
**Robert Pająk** 18:26 Yeah.
**Dan Gomez Blanco** 18:28 So what was the thing like? Basically. So if you.
**Robert Pająk** 18:36 I'm not sure. Yeah.
**Dan Gomez Blanco** 18:38 So it has a Ci task that auto requests reviews from co-owners who are members of the auto or not necessarily approvers on the repo.
So only collaborators can be requested. All right. So then, yeah.
so they need to be added as collaborators individually to each report, be able to assign alright, I see.
I see. But so if we do this, then.
for example, in the Java contract triagers, then in us in that job, instead of assigning it to one person assigns it to the team.
So so if you make the team a collaborator, does that allow you to tag specific people.
**Robert Pająk** 19:40 Yes, as far as I understand. Yes.
because there are. Sec. Each like this is how the groups work. Basically none is added individually, at least as far as I know.
**Dan Gomez Blanco** 19:55 Okay.
**Robert Pająk** 20:03 And here, in this period, we get pushback that people do not want to be added to the treasures because of the current. You know, wording in the community that they are supposed to be responsible.
**Dan Gomez Blanco** 20:14 Okay, I see. So your Pr here is saying, Okay, co-owners, you will add the triagers.
**Robert Pająk** 20:19 Yes.
**Dan Gomez Blanco** 20:30 But do they need to be? Quote owners.
**Robert Pająk** 20:34 These people are already code owners, basically.
So we just need the code owners. We just need to have a way to add code, like to add the automation for code owners, or basically even request reviews, because, as far as I understand right now, it's not even possible.
**Dan Gomez Blanco** 20:50 Oh, I see, of course. Yeah, yeah, yeah, makes sense.
Yeah. I think if we were to change it, I mean, I'll be happy to to change it in the in the guide here, in this responsibilities and privileges, like, you know, maybe yeah, maybe this can be.
Maybe this can just be a bit more.
Yeah. Organizing milestones, for example, and projects is probably something that she Aja's that we can put into the Maintainer.
**Robert Pająk** 21:26 Yes.
**Dan Gomez Blanco** 21:26 Of a maintainer thing right anyways.
**Robert Pająk** 21:28 I agree.
**Dan Gomez Blanco** 21:33 Yeah, okay. So if you open an issue for this, we can. Yeah, I'm sure we can also.
**Robert Pająk** 21:37 So not sure if maybe you should consider that triage is someone that only has privileges, but do not have any responsibilities. The responsibilities are more on the approvals and Maintainer side. That's also, you know.
a 6.
**Dan Gomez Blanco** 21:52 Proposal, I guess, in order to be able to triage.
**Robert Pająk** 22:01 This is a requirement. This is not a responsibility. It should be.
**Dan Gomez Blanco** 22:04 Fair enough. Yeah, fair enough.
Yes, yeah.
Yeah.
They yeah.
But I have a responsibility to be, you know, to join meetings right? And be up to date with well, at least there's 1 to respond to new prs.
An issue is clarifying. Question.
**Robert Pająk** 22:20 Yeah. And and exactly, that was the concern that basically, one of the code owners said that he do not want to respond to peers and issues which are not in the, in the air if in his component, in his area.
That's 1 thing and other thing is that also somebody said that triagers do not need to be a kind of, you know, code related to code. They can be just like, you know, Pm's or Pre. The product owners, so why they should respond to Prs. Still.
even to the current based on the current description.
**Dan Gomez Blanco** 22:58 Right? Okay, yeah. I think you know, we can definitely touch the wording here. And on that, I think at the end of the day. We also want to give people like, you know, a bit more of.
I guess a path of like, you know. What does it mean to be a triager. I think you know.
**Robert Pająk** 23:14 Right now, I think because of the current definition. I don't know how many trailers we have in go. We have 0. I don't know if there's 1 in.net, I'm not sure what's in what's in a in the other, you know. 6.
But my guess, how how many churches do we even have compared.
**Dan Gomez Blanco** 23:33 Yeah, I know. Yeah, I know. For example, python don't even have a team. They just didn't find triage or something that you know.
because at the end of the day they just want the approval. Yeah, that's a good. That's a good point, like Triager, like on the Pr side. If we say, Pr, it's like, you know.
there isn't. Yeah. We're not asking them to review the Pr, because that will probably be on the approval side.
**Robert Pająk** 23:56 Yes.
**Dan Gomez Blanco** 23:57 So, yeah, I think we can make this clearer. I think it should be relatively.
But the question to ask here for me, or the the question to answer is, how can Triages make and so provide value with you know what they do, as in like, you know? Is it something that they can do that they can. They could take some work off like approvers or maintainers.
**Robert Pająk** 24:27 Yes. So even even the applying label stuff, even this thing, can, you know right now, people who are outside, you know, they're not like from my what I see usually. When there's new people contributing to seek. Usually they go straight to the approvals and then to the Maintainers.
**Dan Gomez Blanco** 24:46 Yeah.
**Robert Pająk** 24:47 I haven't seen anyone who just started 1st being a treasure, then a prover, then a Maintainer.
**Dan Gomez Blanco** 24:52 Yeah, yeah, yeah, yeah. So we should probably define a lower entry barrier, maybe. And and.
**Robert Pająk** 25:00 I think it can be also maybe more like the barrier for the prover. I wouldn't say it's very high, but you know it's not low, but I think maybe if it will be if people will see that it is something, you know, maybe there are free, free, like levels of being, you know, a Maintainer, etcetera. So maybe it will also somehow encourage other people to try to contribute more if they see that becoming treasure is, you know not so hard. Also, I do not see that if I remember correctly.
people who become treasures will not be able to, or they can close issues. I'm just thinking if they can do any harm to us if we add too much treasures.
Yes, so I think the most devastating thing they can do. They can just close issues and Prs, which.
**Dan Gomez Blanco** 25:52 My only my only concern about like making it like, Hey, you know, anyone can be a Triager, and then is that the there needs to be some type of like commitment to be involved in some way, right? Because otherwise, people people just like to have a hat and then go like, Oh, yeah, I'm a triage, and there's repo. And then they never show up. They never do any any triaging. And that's also not good. Right? Yeah.
**Robert Pająk** 26:17 So maybe that's so. Maybe that's the reason to have the separate role code owner which will can have, you know, of a component which was a separate proposal. Because it's easier to have this. You know the definition what someone is responsible for, basically, you know, of a sub component in a repository. So maybe creating a new role. Even if on Github it will be the same permissions. Maybe it will be really easier.
**Dan Gomez Blanco** 26:44 Yeah. Can you? Do you want to like open an issue in the community for this? I think? It'll be good to discuss it.
**Robert Pająk** 26:52 I will first, st maybe respond in the issues that was.
**Dan Gomez Blanco** 26:55 Right? Okay, yeah.
**Robert Pająk** 26:58 Not here. Yeah.
**Dan Gomez Blanco** 27:00 And the one that was.
**Robert Pająk** 27:02 I can. Yeah, I can make a summary from our discussion.
**Dan Gomez Blanco** 27:05 In this one. Yeah, cool. Thank you.
**Robert Pająk** 27:07 That's probably going forward with a new role will be the most effective way.
**Dan Gomez Blanco** 27:12 Sounds good.
Don't think this needs to be triage. This is related to this is an interesting one.
This is from the Toc, I don't think we've got even a label to be able to triage this.
Yeah, I'll just leave it without rehaging I guess we're accepting it. And this is basically like we need to have a better way of defining releases for hotel.
And we need to think about that for graduation.
So I might actually had a triage. Accept it.
So done.
And this is report main, we normally, yeah, yeah, this would be, why is it called Github membership Php. Integration with hotel.
and what.
**Robert Pająk** 28:41 Php, yeah, I know. But I'm just looking at the the project. Api request. Qps is high.
**Dan Gomez Blanco** 28:48 I didn't.
**Robert Pająk** 28:50 Oh, gosh!
**Dan Gomez Blanco** 28:59 A hmm, bye, I think what would be the best. I mean, this is related to Php.
I don't want to close it because.
**Robert Pająk** 29:21 Yeah, I know.
**Dan Gomez Blanco** 29:21 And right, but like But I mean, is it even related to the Dpa container? Always run field.
**Robert Pająk** 29:41 Is it a global question? Or is it to? Php, yeah.
**Dan Gomez Blanco** 29:58 Similar issue. Okay.
was the what is php, php, contrip, php, hmm.
I'm assuming they're talking about something related to the SDK policy.
Let's do that for now I'll take care of it, and and that's it, and there's anything else. The rest is related to things that we decided not to label for some reason.
and that's me done the half hour. Yeah.
**Robert Pająk** 31:35 Cool.
**Dan Gomez Blanco** 31:36 I don't think there's anything else. But if you want to stay around and have a chat with Severin.
**Robert Pająk** 31:40 Yeah, I can wait. I can wait here in the background.
**Dan Gomez Blanco** 31:43 Okay, right? See you later. Bye.
**Severin Neumann** 35:53 Hey? Robert! Good morning.
**Robert Pająk** 35:57 Hello! Good morning. We already.
**Severin Neumann** 35:59 Is it only? Is it? Is it only you, or did Dan already leave.
**Robert Pająk** 36:02 Then, then, okay, to leave. I said that I'll just wait for you in case there's something that you we we want to discuss as well as well.
**Severin Neumann** 36:10 No. Did you get through like the the spec issues or.
**Robert Pająk** 36:15 Yes, we did, but you can double check if we haven't missed anything.
**Severin Neumann** 36:19 Yeah, let me. I I don't have anything particular in mind. I just wanted to see if if anyone is still around. But yeah, I mean, have you.
**Robert Pająk** 36:27 So.
**Severin Neumann** 36:28 The triage list is empty.
There's also nothing to follow up. So I think we are fine, right? Oh, there's your Lassi. Every everybody coming late today.
**Juraci Paixão Kröhling** 36:44 Oh, yeah, I'm sorry, folks. I had a meeting.
**Severin Neumann** 36:46 Yeah, I I just joined as well, and Dan already left. So Robert is the only constant.
**Juraci Paixão Kröhling** 36:52 Bye.
**Robert Pająk** 36:55 Yeah, I said that I will wait here on the background if you maybe you have some topics.
**Severin Neumann** 37:00 Not really. I I don't know, I think. Let me check. I did you. You work through the triage list right? Is there anything in community that that needs our intention. I also don't.
Don't think so. So yeah.
**Robert Pająk** 37:17 The one thing which we discussed, maybe just or a heads up in the community issue 2, 7, 9, 3. I'll add it to the chat. I just add that what we summarized, together with Dan and.
**Severin Neumann** 37:30 Which one.
**Robert Pająk** 37:31 I have to add it to the chat. You can share your screen and see ya!
This was going on with my machine.
**Severin Neumann** 37:46 In a second.
There.
you can see that.
**Robert Pająk** 38:02 Yes.
So basically, when trust, I think, added the private repo.
I haven't. I haven't looked very the like the consequences of some same changes, I think, because of the Admin repo is that the code owners the like that, are usually assigned to the Prs and collector, and go, and probably in other repos.
stopped working.
and Admin said that previously they had some work around that instead of creating private repositories, they just created a separate org.
I'm not sure if it's an option here, but it feels like a hack, not a proper solution.
So one of the proposals was to add to all all corners to 3 others.
but it looked like there are so many code owners in the collector that they wouldn't probably want doing it. We tried doing it in go conscript. And you already got feedback that some people do not want to to be seen as a treasure, because the Triager responsibility, according to the community. Docs says that basically, these people are, you know, responsible kind of a product management. And you know.
yeah, no.
etc.
And yeah. And we were still in Java config. They added, every 1, 2, 3 azures but the thing is that we've we were, think, brainstorming the possible solutions. So one of the proposals I think it was by myself. And also it looked promising at initially, was basically to combine the 3 azure role so code owners could fit in there. But basically, these are different personas. And it's even hard to describe the role in a way that will fit both the project management like perspective, like view. Or you know, responsibility as well as someone who is basically a maintainer of one component inside of repository which is usually developer. So we found that probably setting up 2 separate roles and teams will be more clear, even if both teams will have the same permission on the, you know from the security perspective that basically will probably add them both as treasures. Or maybe you have create, maybe just a custom custom permissions in Github, if necessary.
**Severin Neumann** 40:35 I I mean, 1st of all, I I don't think that there needs to be a clear mapping between github permissions, and like like a triage or not necessarily has to be the same as like the triage role in a repository. I'm I'm totally with you on that.
So yeah. So. So I'm I'm just trying to think this through. If we formalize the code owner role.
the I think the the bigger question is like, Where does it sit right? Is it like it's like so so it it. It has always been a little bit of a like a like like be, because our roles are kind of a ladder, right? I mean, there's like you become a member. Then some 6 have triage or approver Maintainer. Whatever right code owner is more like, yeah, you own you own some of like, like, you own some code.
But this is like.
so this is my point of view. I think that someone who is not willing to do triage in a repository has no step up to become an approver or a maintainer. Right if they say like, oh, I only want to focus on my component, then let it be right.
But there's no way from that to become like a maintainer or something like that right? I mean, they would need to prove that they can do more than like take care of one component.
I mean, it's different. If they take care of 5 or 10 components, right? I mean at some level. There, there's a matter of scale, right? I mean, the collector has. I don't know how many components I think it's in in the hundreds, like or in in the like 3 digits. That's very different. But if someone says like, hey? I'm I'm the code owner of like component A, BA and B, and and then do nothing else. I find this very different to someone who says like, Hey, I serve the whole stick as a triager, as an approver that's good.
and my employer or my personal goal is to be maintainer in in this repository. I think that's just different different also from from like, why people are contributing to the project right.
**Robert Pająk** 42:59 Yes.
I just thinking, do we have some code owner? Descriptions? Maybe in Collector I we have for sure one in go country, probably.
**Severin Neumann** 43:11 I think I think the Collector sick also has one, because someone recent, didn't someone from Php. Sick ask the other way other day in the Maintainers Channel.
Yeah, there is. There is something like contract vendors. Western?
Yeah, this was more around contract. Okay?
yeah. I. So so to make make it short. I think I agree with you that we should define code owners as a role.
But we should also make very clear that if someone says, like, Hey, I am the code owner of my vendor, specific component in the open telemetry collector or in the Java instrumentation libraries, or whatever that this is not necessarily the same thing as someone who is doing triage and and approvals and and maintainership right? We appreciate that. And then this is great that you do that. But like, yeah, you carved out your own small universe in the open telemetry project. But but like, if we talk about this letter that that some people like seeing and having transparent, then I would say, like the code owner is like a How are you still like a step to decide without necessarily something where you say, like, Oh, yeah, it's very naturally that, like a code owner suddenly steps up to become a maintainer.
It's different. If they maintain a set like 5 or 10 components, let's let's speak about that. But like.
yeah. But maybe we need to put in an issue for that, and then have a discussion on that how to.
or someone creates a Pr with their opinion. And then we see like how how it goes from there. I think that's more effective than raising an issue.
**Robert Pająk** 45:07 Robert, if if there's anything in the collector in the go repo already that we can build on.
just added it right now in the chat a just to not make a mess right now in the issue.
just trying to find if there's also something in the organization code owner.
**Severin Neumann** 45:35 Yeah, I think that's something we can build on right? I mean, that's.
**Robert Pająk** 45:39 Go, country.
**Severin Neumann** 45:43 I mean, especially since we he didn't.
**Robert Pająk** 45:46 There is something they're receiving, something specification. It talks about code owners, but it doesn't describe them at at all.
Collector collector community, I own I new commercials with code on verbs.
**Severin Neumann** 46:20 I mean the community repo would be the one that's
**Robert Pająk** 46:23 Yes, yes, no! Here we do not schedule it like that.
**Severin Neumann** 46:30 Yeah.
yeah, I think we should just add, like above triage, or the code owner, and copy some of the wording from from the go, or the spec repo.
maybe also add it here to the table.
**Robert Pająk** 46:54 Do you have time to take it and try clicking something? Okay.
**Severin Neumann** 47:00 Not really. But I mean, if if if you have bandwidth, then then let me know. If not, I can see if I can find some time sooner than later. But
**Robert Pająk** 47:09 Just need to sacrifice some other things.
**Severin Neumann** 47:12 Yeah. Yeah. Same. Here.
**Juraci Paixão Kröhling** 47:13 I could open a Pr. For that. But I I'm having trouble getting people looking at my peers already, and so my motivation nowadays is very, very low.
**Robert Pająk** 47:25 Like trust is already involved. Damien is involved. I mean, I will be involved. Savory can be also involved.
So yeah.
**Juraci Paixão Kröhling** 47:34 If it's only about adding a new like role there, I can. I can do that with a proposal. But.
**Severin Neumann** 47:41 Yeah, tag us. And we can already like 5 to discussion. And I know what you mean like right now, it's really like, people are all over the place. And yeah.
**Juraci Paixão Kröhling** 47:57 Alright.
So the idea is above 3 azure and new code owner that only takes care of a specific component. Not yeah.
Yeah.
**Severin Neumann** 48:11 And and that we copy some of the wording that exists already in collector and go contrip.
and then maybe and and if you have open. Tpr, I can. I can try to to come up with wording for them to say like, Hey.
code owner kind of stands out a little bit, because it's not like like a triager or approver who who serves the whole project right.
**Robert Pająk** 48:32 Yeah, it's just a complimentary.
**Severin Neumann** 48:34 It's appreciated. But it's like as long as you say, like, Hey, I focus on this one tiny core of the open telemetry universe. That's fine, but but it's not like So so, and especially you don't have to be a code owner before you can become a triager. Right? May maybe at some point you need to make this this letter a little bit more more obvious. And it's like, Hey, you can go from that role to that role, etc.
**Robert Pająk** 49:03 I see.
**Juraci Paixão Kröhling** 49:04 So sorry. Go ahead.
**Robert Pająk** 49:06 Before we start doing anything we should just wait. What if task responds at all?
**Severin Neumann** 49:11 Yeah, yeah, okay, let's do that. First.st Awesome.
Anything else.
**Robert Pająk** 49:31 Nothing from my side.
**Juraci Paixão Kröhling** 49:32 Cool, wonderful. All right.
**Severin Neumann** 49:40 Awesome.
**Juraci Paixão Kröhling** 49:41 Q. 4.
See you? Then? Yeah, bye-bye.
